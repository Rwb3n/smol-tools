# PDF Splitter

A Python script to break large PDF files into smaller ones.

## Description

This utility allows you to split a large PDF document into multiple smaller PDF files. You can split by a specific number of pages per output file or provide custom page ranges to create precisely the PDF segments you need.

## Requirements

- Python 3.6 or higher
- PyPDF2 library

## Installation

1. Clone this repository or download the script
2. Install the required dependency:

```bash
pip install PyPDF2
```

## Usage

The script provides two primary methods for splitting PDFs:

### Option 1: Split by page count

Divide the PDF into chunks with a specific number of pages per file:

```bash
python pdf_splitter.py input.pdf --pages-per-file 10
```

This will split `input.pdf` into multiple files with 10 pages each.

### Option 2: Split by custom page ranges

Specify exact page ranges for each output file:

```bash
python pdf_splitter.py input.pdf --page-ranges "1-5" "6-10" "11-20"
```

This will create three output files with pages 1-5, 6-10, and 11-20 respectively.

### Additional options:

- `--output-dir` - Specify the output directory (default: "split_output")
- `--prefix` - Set the prefix for output filenames (default: "part")

### Example

```bash
python pdf_splitter.py large_document.pdf --pages-per-file 25 --output-dir "my_chapters" --prefix "chapter"
```

This command will:
- Take `large_document.pdf` as input
- Split it into files with 25 pages each
- Save the output files in the "my_chapters" directory
- Name the files "chapter_1.pdf", "chapter_2.pdf", etc.

## Output

The script creates:
- An output directory (if it doesn't already exist)
- Multiple PDF files with the specified naming scheme
- Console output showing the progress and details of each created file

## License

This project is available under the MIT License.

## Contributing

Contributions, bug reports, and feature requests are welcome!
