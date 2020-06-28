import logging

class Fundshooks:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        response = self.get_response(request)

        # logging.error(vars(response))
        # logging.error( response.content  )

        if str(response.status_code) == "404":
            logging.error(   response.status_code   )
            logging.error(   "===========NOTFOUND")
            logging.error(   "===========NOTFOUND")

            # Other variables or methods
            # response.__setitem__("Access-Control-Allow-Origin", "*")
            # response.__delitem__("Access-Control-Allow-Origin")
            # HttpResponse.__delitem__(header)
            # HttpResponse.setdefault(header, value)
            # HttpResponse.streaming  /// checks if the response is a streaming response or an html regular response

        return response
