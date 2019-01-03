# ConverterDataFormatModule
Converter Data Format Module is a module that converts data from one format to other formats. 
The module reads data in CSV file. And The data can be sorted and grouped according to custom options.
- If you want default data: 
```
python3 main.py \
 -i hotel.csv \
 -o json
```
- If you want sorted data by columns, and ascending, descending:
```
python3 main.py \
 -i hotel.csv \
 -sc name stars \
 -st True, False \
 -o json
```
- If you want grouped data by columns:
```
python3 main.py \
 -i hotel.csv \
 -g name address \
 -o json
```
- If you want sorted and grouped data by columns:
```
python3 main.py \
 -i hotel.csv \
 -sc name stars \
 -st True, False \
 -g name address \
 -o json
```
and validates the data with the following conditions:
- The 'name' column contains only UTF-8 characters. In addition, it converts to Unicode if it contains ASCII code. 
- The 'url' column validates the URL format using 'validators' package.
- The 'stars' column checks type of the value. It only allows numbers and not negative numbers. And the value is between 0 and 5. 

and then, it provides results in JSON or YAML files.
- The module applies a **strategy pattern** to expend other formats.
![class_diagram](https://user-images.githubusercontent.com/3222837/50623403-d55ecb00-0f15-11e9-9731-3adce0e8975d.PNG)
- The module makes two results such valid_hotel_(%datatime) and invalid_hotel_(%datatime).
  - valid_hotel_(%datatime)  : The result of data that has been validated.
  - invalid_hotel_(%datatime): The result of data that has been invalidated. The result will be used to improve the quality of the data.
  
  Additional implemented logger module considering scalability. This helps the operation of service.
 
## Guiding principles
- User friendliness
- Modularity
- Easy extensibility
- Work with Python

## Installation & Requirements
- This module works with Python>3.0. This script is a script that configures the environment for executing the module. The script installs python 3 if python is not installed or if a lower version is installed. Then, It installs necessary python packages.
```
$ sh install_python3.sh
```

## General Guideliens
- **How to run** 
1. Move the project to a directory what you want on the **Debian 9** server. For reference, I ran in the 'admin' directory on Debian 9.
2. Run main.py from '(your path)/convert-data-format-module/src'. Example:
```
$ cd /home/admin/convert-data-format-module/src
```
```
# output_file is .yaml
$ python3 main.py -i hotels.csv -o yaml
```
```
# output_file is .json | sort by name, stars | ascending for name, dscending stars
$ python3 main.py -i hotels.csv -o json -sc name stars -st True False
```
```
# output_file is .yaml | group by stars
$ python3 main.py -i hotels.csv -o yaml -g stars
```
```
# output_file is .yaml | sort by name, stars | ascending for name, dscending stars | group by stars
$ python3 main.py -i hotels.csv -o yaml -sc name stars -st True False -g stars
```
