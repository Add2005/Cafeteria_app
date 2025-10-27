
class Venta:
    
    def __init__(self,  TotalVenta, FechaHora, IdCliente, IdEmpleado, id = None):
        self.id = id
        self.TotalVenta = TotalVenta
        self.FechaHora = FechaHora
        self.IdCliente = IdCliente
        self.IdEmpleado = IdEmpleado