from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class Service1(ServiceBase):
    @rpc(_returns=Unicode)
    def get_current_time(ctx):
        return str(datetime.datetime.now())

    @rpc(Unicode, _returns=Unicode)
    def get_weather_info(ctx, city_name):
        # Call an external SOAP service to get weather information
        client = zeep.Client('http://www.webservicex.com/globalweather.asmx?WSDL')
        response = client.service.GetWeather(city_name)
        return str(response)
    
application = Application([Service1], 'http://localhost:8000/', in_protocol=Soap11(), out_protocol=Soap11())
wsgi_application = WsgiApplication(application)
