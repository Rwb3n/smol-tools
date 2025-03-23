#!/usr/bin/env python3
"""
PDF Splitter - A script to break a large PDF into smaller PDFs

This script takes a large PDF file and splits it into multiple smaller PDF files.
You can split by a specific number of pages per output file or provide custom
page ranges.

Requirements:
    pip install PyPDF2
"""

import os
import argparse
from PyPDF2 import PdfReader, PdfWriter


def split_pdf_by_page_count(input_pdf, output_directory, pages_per_file, output_prefix):
    """Split a PDF into multiple PDFs with a specific number of pages per file."""
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Read the input PDF
    pdf_reader = PdfReader(input_pdf)
    total_pages = len(pdf_reader.pages)
    
    # Calculate how many output files we'll create
    num_output_files = (total_pages + pages_per_file - 1) // pages_per_file
    
    print(f"Splitting {input_pdf} ({total_pages} pages) into {num_output_files} files...")
    
    # Create each output PDF
    for i in range(num_output_files):
        start_page = i * pages_per_file
        end_page = min((i + 1) * pages_per_file, total_pages)
        
        pdf_writer = PdfWriter()
        
        # Add pages to the output PDF
        for page_num in range(start_page, end_page):
            pdf_writer.add_page(pdf_reader.pages[page_num])
        
        # Generate output filename
        output_filename = f"{output_prefix}_{i+1}.pdf"
        output_path = os.path.join(output_directory, output_filename)
        
        # Write the output PDF
        with open(output_path, "wb") as output_file:
            pdf_writer.write(output_file)
        
        print(f"Created: {output_path} (Pages {start_page+1}-{end_page})")


def split_pdf_by_ranges(input_pdf, output_directory, page_ranges, output_prefix):
    """Split a PDF into multiple PDFs based on specified page ranges."""
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Read the input PDF
    pdf_reader = PdfReader(input_pdf)
    total_pages = len(pdf_reader.pages)
    
    print(f"Splitting {input_pdf} ({total_pages} pages) into {len(page_ranges)} files...")
    
    # Process each page range
    for i, page_range in enumerate(page_ranges):
        # Parse the range (format: "start-end")
        parts = page_range.split("-")
        if len(parts) != 2:
            print(f"Warning: Invalid range format '{page_range}'. Expected 'start-end'.")
            continue
        
        try:
            start_page = int(parts[0]) - 1  # Convert to 0-based index
            end_page = int(parts[1])        # End page is exclusive
            
            if start_page < 0 or end_page > total_pages or start_page >= end_page:
                print(f"Warning: Invalid page range {page_range}. Skipping.")
                continue
            
            pdf_writer = PdfWriter()
            
            # Add pages to the output PDF
            for page_num in range(start_page, end_page):
                pdf_writer.add_page(pdf_reader.pages[page_num])
            
            # Generate output filename
            output_filename = f"{output_prefix}_{i+1}.pdf"
            output_path = os.path.join(output_directory, output_filename)
            
            # Write the output PDF
            with open(output_path, "wb") as output_file:
                pdf_writer.write(output_file)
            
            print(f"Created: {output_path} (Pages {start_page+1}-{end_page})")
        
        except ValueError:
            print(f"Warning: Invalid page numbers in range '{page_range}'. Skipping.")


def main():
    # Set up command line argument parser
    parser = argparse.ArgumentParser(description="Split a large PDF into smaller PDFs")
    parser.add_argument("input_pdf", help="Path to the input PDF file")
    parser.add_argument("--output-dir", default="split_output", help="Directory to save output files (default: split_output)")
    parser.add_argument("--prefix", default="part", help="Prefix for output filenames (default: part)")
    
    # Create a mutually exclusive group for splitting method
    split_method = parser.add_mutually_exclusive_group(required=True)
    split_method.add_argument("--pages-per-file", type=int, help="Number of pages per output file")
    split_method.add_argument("--page-ranges", nargs="+", help="Specific page ranges (e.g., '1-5' '6-10' '11-15')")
    
    args = parser.parse_args()
    
    # Validate input file
    if not os.path.exists(args.input_pdf):
        print(f"Error: Input file '{args.input_pdf}' not found.")
        return
    
    # Split the PDF based on the chosen method
    if args.pages_per_file:
        split_pdf_by_page_count(args.input_pdf, args.output_dir, args.pages_per_file, args.prefix)
    else:
        split_pdf_by_ranges(args.input_pdf, args.output_dir, args.page_ranges, args.prefix)
    
    print("PDF splitting complete!")


if __name__ == "__main__":
    main()
