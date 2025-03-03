from ninja import Router


router = Router(tags=["API1"])

@router.get("/api/add")
def add(request, x: float, y: float):
    return {"result": x + y +3}
