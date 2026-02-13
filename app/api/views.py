from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .dynamo import get_table


@api_view(["GET"])
def health(request):
    return Response({"status": "ok"})


@api_view(["GET"])
def customer_get(request, customer_id: int):
    table = get_table()
    resp = table.get_item(Key={"CustomerID": int(customer_id)})
    item = resp.get("Item")
    if not item:
        return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    return Response(item)


@api_view(["POST"])
def customer_put(request):
    """
    Body example:
    {
      "CustomerID": 12345,
      "recency_days": 10,
      "frequency": 4,
      "monetary_value": 250.75
    }
    """
    data = request.data
    if "CustomerID" not in data:
        return Response({"detail": "CustomerID is required"}, status=status.HTTP_400_BAD_REQUEST)

    table = get_table()
    data["CustomerID"] = int(data["CustomerID"])
    table.put_item(Item=data)

    return Response({"status": "saved", "CustomerID": data["CustomerID"]})
