# Barcode Service
Simple and small python service designed to generate and read Barcode, QRCode, Aztec Code, DataMatrix.

## Demo
	
> https://barcode.adrox.xyz/api/v1/  
> https://barcode.adrox.xyz/api/v1/docs

## Requirements and dependencies
The website was written using Python 3.8 and FastAPI.  
The dependencies are listed in the `pyproject.toml` file.  

## Installation
By default, the application is served on port 8000.

### Local
To run the application locally, install the dependencies using [poetry](https://python-poetry.org/) 

```
poetry install
```

file and then execute the command 

```
uvicorn app.main:app --reload
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
To run the application on localhost from docker-compose, go to the `deployment/docker-compose` folder and execute the command:

Windows:
```
$env:URL="localhost"; docker-compose -f docker-compose.yml up
```

Linux, macOS:
```
URL="localhost" docker-compose -f .\docker-compose.yml up
```

Traefik automatically manages the SSL certificate generating the let's encrypt certificate. The certificate is generated for `example@example.com`, please change if necessary.  

After launch, it will be available at https://localhost/api/v1/

### Kubernetes example
Running the application using kubernetes requires having installed helm and installing a traefik with it.  
Installation of the traefik can be performed using the following commands:
```
$ helm repo add traefik https://containous.github.io/traefik-helm-chart
$ helm repo update
$ helm install traefik traefik/traefik
```

Then go to the `deployment/kubernetes` folder and execute the following commands:
```
$ helm upgrade traefik traefik/traefik --values 000-values.yaml
$ kubectl apply -f 001-deployment.yaml
```

Traefik automatically manages the SSL certificate generating the let's encrypt certificate. The certificate is generated for `example@example.com`, please change if necessary.  


In order for the application to be launched on an address other than `localhost`, localhost addresses should be changed in the `001-deployment.yaml` file to the target address of your choice.

Without changing the configuration and parameters, the application will be available at: `https://localhost`.
## Requests
Swagger is available at `/docs` path.

### List of available requests:

#### barcode
Request type: __post__  
Request path: __/api/v1/barcode/generate__  
Data:      
>barcode_type: str  [values: EAN8,EAN13,EAN14,UPCA,JAN,ISBN10,ISBN13,ISSN,Code39,Code128,PZN]  
>barcode_message: str [Just a message]

#### qrcode
Request type: __post__  
Request path: __/api/v1/qrcode/generate__   
Data:  
>qrcode_scale: int [Image scale between 1 to int constraint]  
>qrcode_message: str  [Just a message]  
>qrcode_error_correct: Optional[str] = None [L (7% compression), M (15% compression), Q (25% compression), H (30% compression) or just remove this parameter from request]  

Request type: __post__  
Request path: __/api/v1/qrcode/decrypt__  
Data:      
>file: string($binary) [Just a file]  

#### aztec
Request type: __post__  
Request path: __/api/v1/aztec/generate__  
Data:  
>aztec_code_scale: int  [Image scale between 1 to int constraint]  
>aztec_code_message: str [Just a message]  

#### datamatrix
Request type: __post__  
Request path: __/api/v1/datamatrix/generate__  
Data:  
>data_matrix_message: str [Just a message] 

Request type: __post__  
Request path: __/api/v1/datamatrix/decrypt__  
Data:      
>file: string($binary) [Just a file]  

## License
The application is available under the GNU GENERAL PUBLIC LICENSE.
