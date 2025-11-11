from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from .models import Product


def product_lookup(request):
    """Simple view with a form to enter UPC and display product name + price.

    This view remains for non-JavaScript fallback. A separate JSON endpoint
    is provided for the dynamic scanning UI (AJAX).
    """
    product = None
    query = ""
    if request.method == "POST":
        query = request.POST.get("upc", "").strip()
        if query:
            product = Product.objects.filter(upc=query).first()

    return render(request, "db/product_lookup.html", {"product": product, "query": query})


@csrf_exempt
def product_lookup_json(request):
    """JSON API endpoint to lookup a product by UPC.

    Accepts POST with either form-encoded data or JSON body: {"upc": "..."}.
    Returns 200 + product data when found, 404 when not found, 400 for bad
    requests.
    """
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)

    upc = ""
    # Try JSON body first
    try:
        if request.content_type and "application/json" in request.content_type:
            payload = json.loads(request.body.decode() or "{}")
            upc = (payload.get("upc") or payload.get("code") or "").strip()
    except Exception:
        upc = ""

    # Fallback to form data
    if not upc:
        upc = (request.POST.get("upc") or request.POST.get("code") or "").strip()

    if not upc:
        return JsonResponse({"error": "upc required"}, status=400)

    product = Product.objects.filter(upc=upc).first()
    if not product:
        return JsonResponse({"found": False, "upc": upc}, status=404)

    return JsonResponse({
        "found": True,
        "upc": product.upc,
        "name": product.name,
        "price": str(product.price),
    })
