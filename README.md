# md2pdf
A tool that convert from markdown file(s) to pdf

#### Dependencies

* Python 3.x
* [Pandoc](https://github.com/jgm/pandoc)
* [LaTex](https://www.latex-project.org)

#### Installation

The key point you may make sure that your **Pandoc** and **LaTex** were properly installed, work well. Also remember we use python 3.x as our environment.

For convenience, add **md2pdf** to your binary soft folder:

```bash
sudo cp md2pdf.py /usr/local/bin/md2pdf
```

Usage:

* From folder

  ```bash
  md2pdf -d your_md_dir -o dist_dir/filename.pdf
  ```
  **Note: **In this way, all markdown files will be process in natural ordering.

* From file(s)

  ```bash
  md2pdf -i 1.md -i 2.md -o dist_dir/filename.pdf
  ```

  

