# utilities

Groups various python helpers.

## attendance_finder

@description:
This is an ad-hoc solution for producing attendance
sheet when the LMS gives you for each lecture a csv
file with the names in the first columns.
@arguments:
**input1: a directory where all csv files have been
downloaded
**input2: the name  of the file where you want the
result to be saved as csv file
@dependencies:
pandas

## latex_column_remover

Removes column i from a latex table

## Qr code

Python wrappers to generate QR codes or read QR code from a file.
Requires the packages pypng, pyqrcode and pyzbar.

## Tikz_extractor

Get all tikz envirements in all latex files contained in a directory.
Tikz environments begin with "\begin{tikzpicture}"
and end with"\end{tikzpicture}". They are not supposed to be
contained in each other.

## Translate_helper

Helps translate a text by giving which words are used the most often
Common phrases (up to  depth words) are presented.
