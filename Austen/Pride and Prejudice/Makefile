SOURCE = pride-and-prejudice

make:
	pdflatex $(SOURCE).tex -output-format=pdf
	make clean

epub:
	pandoc -s $(SOURCE).tex -o $(SOURCE).epub

clean:
	rm -rf  $(TARGET) *.class *.html *.log *.aux *.toc *.out
