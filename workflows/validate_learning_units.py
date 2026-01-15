#!/usr/bin/env python3
"""
Validate learning unit YAML files against the defined schema.

Usage:
    python validate_learning_units.py k8s/**/*.yaml
    python validate_learning_units.py --strict k8s/pods101/*.yaml
"""

import sys
import yaml
from pathlib import Path
from typing import Dict, List, Any, Tuple


class Colors:
    """ANSI color codes for terminal output."""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'


def validate_metadata(data: Dict, filepath: str) -> List[str]:
    """Validate metadata section."""
    errors = []
    metadata = data.get('metadata', {})
    
    required_fields = ['slug', 'title', 'topic', 'order_index', 'type', 'difficulty', 'description']
    for field in required_fields:
        if field not in metadata:
            errors.append(f"Missing required metadata field: {field}")
    
    # Validate type
    if metadata.get('type') not in ['coding', 'conceptual']:
        errors.append(f"Invalid type: {metadata.get('type')}. Must be 'coding' or 'conceptual'")
    
    # Validate difficulty
    if metadata.get('difficulty') not in ['beginner', 'intermediate', 'advanced']:
        errors.append(f"Invalid difficulty: {metadata.get('difficulty')}")
    
    # Validate title length
    if len(metadata.get('title', '')) > 50:
        errors.append(f"Title too long ({len(metadata['title'])} chars). Max 50 characters")
    
    # Validate slug format
    slug = metadata.get('slug', '')
    if not slug.islower() or ' ' in slug:
        errors.append(f"Slug must be lowercase with hyphens only: {slug}")
    
    return errors


def validate_conceptual_unit(data: Dict, filepath: str) -> List[str]:
    """Validate conceptual/quiz type unit."""
    errors = []
    metadata = data.get('metadata', {})
    
    # Check description length
    description = metadata.get('description', '')
    desc_length = len(description)
    if desc_length < 1500:
        errors.append(f"Conceptual description too short ({desc_length} chars). Minimum 1500 characters")
    elif desc_length > 3500:
        errors.append(f"Conceptual description too long ({desc_length} chars). Maximum 3500 characters")
    
    # Validate quizzes
    quizzes = data.get('quizzes')
    if not quizzes:
        errors.append("Conceptual units must have quizzes")
    elif len(quizzes) < 3:
        errors.append(f"Too few quiz questions ({len(quizzes)}). Minimum 3 questions")
    elif len(quizzes) > 6:
        errors.append(f"Too many quiz questions ({len(quizzes)}). Maximum 6 questions")
    else:
        # Validate each quiz question
        for i, quiz in enumerate(quizzes, 1):
            if 'id' not in quiz:
                errors.append(f"Quiz {i} missing 'id' field")
            if 'question' not in quiz:
                errors.append(f"Quiz {i} missing 'question' field")
            if 'options' not in quiz or len(quiz['options']) != 4:
                errors.append(f"Quiz {i} must have exactly 4 options")
            
            # Check for answers in public quiz (security issue)
            if 'answer' in quiz or 'correct' in quiz:
                errors.append(f"Quiz {i} contains answer in public section! Move to _solution")
    
    # Validate _solution section
    solution = data.get('_solution', {})
    if not solution.get('quiz_answers'):
        errors.append("Missing quiz_answers in _solution section")
    if not solution.get('quiz_explanations'):
        errors.append("Missing quiz_explanations in _solution section")
    
    # Ensure code fields are null for conceptual
    if data.get('editor_config') is not None:
        errors.append("Conceptual units should have editor_config: null")
    if solution.get('code_solution') is not None:
        errors.append("Conceptual units should have code_solution: null")
    if solution.get('validation_script') is not None:
        errors.append("Conceptual units should have validation_script: null")
    
    return errors


def validate_coding_unit(data: Dict, filepath: str) -> List[str]:
    """Validate coding type unit."""
    errors = []
    metadata = data.get('metadata', {})
    
    # Check steps
    steps = metadata.get('steps')
    if not steps:
        errors.append("Coding units must have steps")
    elif len(steps) < 4:
        errors.append(f"Too few steps ({len(steps)}). Minimum 4 steps")
    elif len(steps) > 8:
        errors.append(f"Too many steps ({len(steps)}). Maximum 8 steps")
    
    # Validate editor_config
    editor_config = data.get('editor_config')
    if not editor_config:
        errors.append("Coding units must have editor_config")
    elif 'language' not in editor_config:
        errors.append("editor_config missing 'language' field")
    elif 'initial_code' not in editor_config:
        errors.append("editor_config missing 'initial_code' field")
    
    # Validate _solution section
    solution = data.get('_solution', {})
    if not solution.get('code_solution'):
        errors.append("Missing code_solution in _solution section")
    if not solution.get('validation_script'):
        errors.append("Missing validation_script in _solution section")
    
    # Ensure quiz fields are null for coding
    if data.get('quizzes') is not None:
        errors.append("Coding units should have quizzes: null")
    if solution.get('quiz_answers') is not None:
        errors.append("Coding units should have quiz_answers: null")
    if solution.get('quiz_explanations') is not None:
        errors.append("Coding units should have quiz_explanations: null")
    
    return errors


def validate_file(filepath: Path) -> Tuple[bool, List[str]]:
    """Validate a single YAML file."""
    errors = []
    
    try:
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)
        
        if not data:
            return True, []  # Empty file, skip
        
        # Check if it's a learning unit (has metadata)
        if 'metadata' not in data:
            return True, []  # Not a learning unit, skip
        
        # Validate metadata
        errors.extend(validate_metadata(data, str(filepath)))
        
        # Type-specific validation
        unit_type = data.get('metadata', {}).get('type')
        if unit_type == 'conceptual':
            errors.extend(validate_conceptual_unit(data, str(filepath)))
        elif unit_type == 'coding':
            errors.extend(validate_coding_unit(data, str(filepath)))
        
        return len(errors) == 0, errors
        
    except yaml.YAMLError as e:
        return False, [f"YAML parsing error: {e}"]
    except Exception as e:
        return False, [f"Unexpected error: {e}"]


def main():
    """Main validation function."""
    if len(sys.argv) < 2:
        print(f"{Colors.RED}Usage: {sys.argv[0]} <yaml_files...>{Colors.RESET}")
        sys.exit(1)
    
    files = []
    for arg in sys.argv[1:]:
        if arg.startswith('--'):
            continue  # Skip flags
        path = Path(arg)
        if path.is_file() and path.suffix in ['.yaml', '.yml']:
            files.append(path)
        elif path.is_dir():
            files.extend(path.rglob('*.yaml'))
            files.extend(path.rglob('*.yml'))
    
    if not files:
        print(f"{Colors.YELLOW}No YAML files found{Colors.RESET}")
        sys.exit(0)
    
    print(f"{Colors.BLUE}Validating {len(files)} YAML files...{Colors.RESET}\n")
    
    total_files = 0
    passed_files = 0
    failed_files = 0
    
    for filepath in sorted(files):
        total_files += 1
        is_valid, errors = validate_file(filepath)
        
        if is_valid:
            print(f"{Colors.GREEN}✓{Colors.RESET} {filepath.relative_to(Path.cwd())}")
            passed_files += 1
        else:
            print(f"{Colors.RED}✗{Colors.RESET} {filepath.relative_to(Path.cwd())}")
            for error in errors:
                print(f"  {Colors.RED}→{Colors.RESET} {error}")
            failed_files += 1
    
    print(f"\n{Colors.BLUE}{'='*60}{Colors.RESET}")
    print(f"Total: {total_files} | {Colors.GREEN}Passed: {passed_files}{Colors.RESET} | {Colors.RED}Failed: {failed_files}{Colors.RESET}")
    
    if failed_files > 0:
        sys.exit(1)
    else:
        print(f"\n{Colors.GREEN}All learning units are valid!{Colors.RESET}")
        sys.exit(0)


if __name__ == '__main__':
    main()
