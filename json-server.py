import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status

from views import get_all_orders, get_single_order, create_order, delete_order
from views import update_metal


class JSONServer(HandleRequests):
    """Server class to handle incoming HTTP requests for shipping ships"""

    def do_GET(self):
        """Handle GET requests from a client"""

        response_body = ""
        url = self.parse_url(self.path)

        if url["requested_resource"] == "orders":
            if url["pk"] != 0:
                try:
                    response_body = get_single_order(url["pk"])
                    return self.response(response_body, status.HTTP_200_SUCCESS.value)

                except TypeError:
                    return self.response(
                        f"Order with id {url['pk']} not found",
                        status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
                    )

            response_body = get_all_orders()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)

        else:
            return self.response(
                "Requested resource not found",
                status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
            )

    def do_POST(self):
        """Handle POST requests from a client"""

        # Parse the URL
        url = self.parse_url(self.path)

        # Get the request body JSON for the new data
        content_len = int(self.headers.get("content-length", 0))
        request_body = self.rfile.read(content_len)
        request_body = json.loads(request_body)

        if url["requested_resource"] == "orders":
            try:
                new_order_id = create_order(request_body)
                if new_order_id is not None:
                    return self.response(
                        "",
                        status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value,
                    )
            except KeyError:
                return self.response(
                    "Error creating order: Invalid data format. Need a metal_id, style_id, and size_id",
                    status.HTTP_400_CLIENT_ERROR_BAD_REQUEST_DATA.value,
                )

        return self.response(
            "Requested resource not found",
            status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
        )

    def do_DELETE(self):
        """Handle DELETE requests from a client"""

        url = self.parse_url(self.path)
        pk = url["pk"]

        if url["requested_resource"] == "orders":
            if pk != 0:
                successfully_deleted = delete_order(pk)
                if successfully_deleted:
                    return self.response(
                        "", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value
                    )

        # If the requested resource is not "orders" or pk is 0 not created
        return self.response(
            "Requested resource not found",
            status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
        )

    def do_PUT(self):
        """Handle PUT requests from a client"""

        # Parse the URL and get the primary key
        url = self.parse_url(self.path)
        pk = url["pk"]

        # Get the request body JSON for the new data
        content_len = int(self.headers.get("content-length", 0))
        request_body = self.rfile.read(content_len)
        request_body = json.loads(request_body)

        if url["requested_resource"] == "metals":
            if pk != 0:
                try:
                    successfully_updated = update_metal(pk, request_body)
                    if successfully_updated:
                        return self.response(
                            "",
                            status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value,
                        )
                except KeyError:
                    return self.response(
                        "Error updating metal: Invalid data format. Need a name and price",
                        status.HTTP_400_CLIENT_ERROR_BAD_REQUEST_DATA.value,
                    )

        # If the requested resource is not "orders" or pk is 0 not created
        return self.response(
            "Requested resource not found",
            status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
        )


#
# THE CODE BELOW THIS LINE IS NOT IMPORTANT FOR REACHING YOUR LEARNING OBJECTIVES
#
def main():
    host = ""
    port = 8000
    HTTPServer((host, port), JSONServer).serve_forever()


if __name__ == "__main__":
    main()
