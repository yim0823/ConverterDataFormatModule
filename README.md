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
- The module makes two results such valid_hotel_(%datatime) and invalid_hotel_(%datatime).
  - valid_hotel_(%datatime)  : The result of data that has been validated.
  - invalid_hotel_(%datatime): The result of data that has been invalidated. The result will be used to improve the quality of the data.

 
