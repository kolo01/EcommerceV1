from api.serializers.cart_serializer import CartSerializer
from cart.models import CartModel
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from product.models import ProductModel
from rest_framework.decorators import action
class CartViewset(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = CartModel.objects.all()

    # Add methods for CRUD operations here if needed
    def create (self,request ):
        data = JSONParser().parse(request)
        products = data["product"]
        price = 0
        for product in products:
            
            product_found = ProductModel.objects.get(id=product)
            
            price = price + product_found.price
        data["total_amount"] = price
        serializer = CartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['patch'])
    def update_cart(self, request, pk= None):
        if pk :
            cart = CartModel.objects.get(pk=pk)
            data = JSONParser().parse(request)
            products = data["product"]
            price = 0
            for product in products:
                product_found = ProductModel.objects.get(id=product)
                price = price + product_found.price
            if (cart.total_amount == 0) :
                print("amount vide")
                data["total_amount"] = price
                serializer = CartSerializer(cart, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif(cart.total_amount == price) :
                print("amount egale")
                serializer = CartSerializer(cart, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({"id":"Id inconnu"}, status=status.HTTP_400_BAD_REQUEST)
                
            elif(cart.total_amount - price) > 0:
                print("amount ajout")
                data["total_amount"] = cart.total_amount - price
                serializer = CartSerializer(cart, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({"id":"Id inconnu"}, status=status.HTTP_400_BAD_REQUEST)
                
            else:
                print("amount ")
                cart.total_amount = 0
                serializer = CartSerializer(cart, data=cart, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({"id":"Id inconnu"}, status=status.HTTP_400_BAD_REQUEST)
                
        else:
            return Response({"id":"Id inconnu"}, status=status.HTTP_400_BAD_REQUEST)

        
   