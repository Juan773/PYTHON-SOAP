from zeep import Client

cliente = Client(wsdl='http://www.dneonline.com/calculator.asmx?WSDL')
print(cliente.service.Multiply(4,10))
print(cliente.service.Add(4,10))
print(cliente.service.Divide(4,10))
print(cliente.service.Subtract(4,10))