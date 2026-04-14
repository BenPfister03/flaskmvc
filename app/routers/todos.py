from fastapi import Request
from fastapi.responses import HTMLResponse
from app.dependencies.session import SessionDep
from app.dependencies.auth import AuthDep
from . import router, templates

@router.get("/todos", response_class=HTMLResponse)
async def todos_view(
    request: Request,
    user: AuthDep,
    db: SessionDep
):
    return templates.TemplateResponse(
        request=request,
        name="todos.html",
        context={
            "user": user
        }
    )