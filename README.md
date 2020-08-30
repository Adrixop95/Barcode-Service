# BarcodeGenerator
Simple and small python service designed to generate Barcode, QRCode, Aztec Code, DataMatrix.

## Demo
	
> https://barcode.adrox.xyz  
> https://barcode.adrox.xyz/docs

## Requirements and dependencies
The website was written using Python 3.8 and FastAPI.  
The dependencies are listed in the `requirements.txt` file.  

## Installation
By default, the application is served on port 8000.

### Local
To run the application locally, install the dependencies from the `requirements.txt` 

```
pip install -r requirements.txt
```

file and then execute the command 

```
uvicorn main:app --reload
```

in the application's root directory.

### Docker
Run the container from the available registry.

```
docker run -p 8000:8000 adrixop95/barcodegenerator:latest
```

If you want, you can maintain the consistency of the generated codes by mounting the following folders:
- /app/aztec
- /app/barcode
- /app/qrcode
- /app/datamatrix

The service does not have any environment variables.

### docker-compose example
To run the application on localhost from docker-compose, execute the command:

Windows:
```
$env:URL="localhost"; docker-compose -f docker-compose.yml up
```

Linux, macOS:
```
URL="localhost" docker-compose -f .\docker-compose.yml up
```

After launch, it will be available at https://localhost

## Requests
Swagger is available at `/docs` path.

### List of available requests:
Request type: __post__  
Request path: __/barcode__  
Data:      
>barcode_type: str  [values: EAN8,EAN13,EAN14,UPCA,JAN,ISBN10,ISBN13,ISSN,Code39,Code128,PZN]  
>barcode_message: str [Just a message]

<br/><br/>

Request type: __post__  
Request path: __/qrcode__   
Data:  
>qrcode_scale: int [Image scale between 1 to int constraint]  
>qrcode_message: str  [Just a message]  
>qrcode_error_correct: Optional[str] = None [L (7% compression), M (15% compression), Q (25% compression), H (30% compression) or just remove this parameter from request]  

<br/><br/>

Request type: __post__  
Request path: __/aztec__  
Data:  
>aztec_code_scale: int  [Image scale between 1 to int constraint]  
>aztec_code_message: str [Just a message]  

<br/><br/>

Request type: __post__  
Request path: __/datamatrix__  
Data:  
>data_matrix_message: str [Just a message] 

## License
The application is available under the GNU GENERAL PUBLIC LICENSE.
