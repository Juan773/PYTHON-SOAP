from zeep import Client

cliente = Client(wsdl='http://www.dneonline.com/calculator.asmx?WSDL')
print(cliente.service.Multiply(2,10))
print(cliente.service.Add(2,10))
print(cliente.service.Divide(10,2))
print(cliente.service.Subtract(10,2))