#!/usr/bin/env python3
"""
Check content quality metrics for learning units.

Usage:
    python check_content_quality.py
    python check_content_quality.py --format=markdown
"""

import sys
import yaml
from pathlib import Path
from typing import Dict, List, Tuple


class QualityMetrics:
    """Calculate quality metrics for learning units."""
    
    def __init__(self):
        self.total_units = 0
        self.conceptual_units = 0
        self.coding_units = 0
        self.short_descriptions = []
        self.missing_code_examples = []
        self.insufficient_quizzes = []
        self.excellent_units = []
    
    def analyze_file(self, filepath: Path):
        """Analyze a single file."""
        try:
            with open(filepath, 'r') as f:
                data = yaml.safe_load(f)
            
            if not data or 'metadata' not in data:
                return  # Not a learning unit
            
            self.total_units += 1
            metadata = data.get('metadata', {})
            unit_type = metadata.get('type')
            description = metadata.get('description', '')
            
            if unit_type == 'conceptual':
                self.conceptual_units += 1
                
                # Check description length
                desc_length = len(description)
                if desc_length < 1500:
                    self.short_descriptions.append((filepath.name, desc_length))
                
                # Check for code examples
                if '```' not in description:
                    self.missing_code_examples.append(filepath.name)
                
                # Check quiz count
                quizzes = data.get('quizzes', [])
                if len(quizzes) < 3:
                    self.insufficient_quizzes.append((filepath.name, len(quizzes)))
                
                # Mark excellent units
                if desc_length >= 2000 and '```' in description and len(quizzes) >= 5:
                    self.excellent_units.append(filepath.name)
            
            elif unit_type == 'coding':
                self.coding_units += 1
        
        except Exception as e:
            pass  # Skip problematic files
    
    def print_report(self, format='text'):
        """Print quality report."""
        if format == 'markdown':
            self._print_markdown_report()
        else:
            self._print_text_report()
    
    def _print_text_report(self):
        """Print text format report."""
        print("=" * 70)
        print("CONTENT QUALITY REPORT")
        print("=" * 70)
        print(f"\nTotal Learning Units: {self.total_units}")
        print(f"  - Conceptual: {self.conceptual_units}")
        print(f"  - Coding: {self.coding_units}")
        
        if self.short_descriptions:
            print(f"\n⚠️  Short Descriptions ({len(self.short_descriptions)}):")
            for name, length in self.short_descriptions:
                print(f"  - {name}: {length} chars (min: 1500)")
        
        if self.missing_code_examples:
            print(f"\n⚠️  Missing Code Examples ({len(self.missing_code_examples)}):")
            for name in self.missing_code_examples:
                print(f"  - {name}")
        
        if self.insufficient_quizzes:
            print(f"\n⚠️  Insufficient Quizzes ({len(self.insufficient_quizzes)}):")
            for name, count in self.insufficient_quizzes:
                print(f"  - {name}: {count} quizzes (min: 3)")
        
        if self.excellent_units:
            print(f"\n✨ Excellent Units ({len(self.excellent_units)}):")
            for name in self.excellent_units:
                print(f"  - {name}")
        
        print("\n" + "=" * 70)
    
    def _print_markdown_report(self):
        """Print markdown format report."""
        print(f"### 📊 Total Learning Units: {self.total_units}")
        print(f"- **Conceptual**: {self.conceptual_units}")
        print(f"- **Coding**: {self.coding_units}")
        
        if self.short_descriptions:
            print(f"\n### ⚠️ Short Descriptions ({len(self.short_descriptions)})")
            for name, length in self.short_descriptions:
                print(f"- `{name}`: {length} chars (min: 1500)")
        
        if self.missing_code_examples:
            print(f"\n### ⚠️ Missing Code Examples ({len(self.missing_code_examples)})")
            for name in self.missing_code_examples:
                print(f"- `{name}`")
        
        if self.insufficient_quizzes:
            print(f"\n### ⚠️ Insufficient Quizzes ({len(self.insufficient_quizzes)})")
            for name, count in self.insufficient_quizzes:
                print(f"- `{name}`: {count} quizzes (min: 3)")
        
        if self.excellent_units:
            print(f"\n### ✨ Excellent Units ({len(self.excellent_units)})")
            for name in self.excellent_units:
                print(f"- `{name}`")


def main():
    """Main function."""
    format = 'text'
    if '--format=markdown' in sys.argv:
        format = 'markdown'
    
    metrics = QualityMetrics()
    
    # Scan all YAML files in k8s directory
    k8s_path = Path('k8s')
    if not k8s_path.exists():
        print("Error: k8s/ directory not found")
        sys.exit(1)
    
    for yaml_file in k8s_path.rglob('*.yaml'):
        metrics.analyze_file(yaml_file)
    
    metrics.print_report(format)


if __name__ == '__main__':
    main()
