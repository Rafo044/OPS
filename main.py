"""Əsas servislər UserService və OrderService monolitik architekturada"""

from fastapi import FastAPI
from loguru import logger
from pydantic import ValidationError
from tortoise.exceptions import DBConnectionError, DoesNotExist, OperationalError

from database import close_db, connection
from order import Order
from user import User
from validator import OrderValidator, UserValidator

logger.add("main.log", rotation="10 MB", retention="10 days")

app = FastAPI()


@app.on_event("startup")
async def create_connection():
    """Bağlantı yaratmaq üçün"""
    try:
        await connection()
    except DBConnectionError as e:
        if isinstance(e, DBConnectionError):
            logger.error(f"Database ilə baglantı yaradıla bilmədi: {e}")
        else:
            logger.error(
                f"Bu xətanın niyə baş verdiyi haqqında heç bir fikrim yoxdu: {e}"
            )


@app.post("/create_user")
async def create_user(items: dict):
    """İstifadəçi yaratmaq üçün
    Args:
        items (dict): İstifadəçi məlumatları

    Returns:
        User: Yaradılmış istifadəçi
    """
    try:
        validated_items = UserValidator.model_validate(items)
        await User.create(**validated_items.dict())
        return validated_items
    except (ValidationError, OperationalError) as e:
        if isinstance(e, ValidationError):
            logger.error(f"Məlumatın dogrulanması zamanı xəta yarandı: {e}")
        if isinstance(e, OperationalError):
            logger.error(f"Database də işləmə zamanı xəta yarandı: {e}")
        else:
            logger.error(
                f"Bu xətanın niyə baş verdiyi haqqında heç bir fikrim yoxdu: {e}"
            )


@app.post("/create_order")
async def create_order(items: dict):
    """Sifariş yaratmaq üçün
    Args:
        items (dict): Sifariş məlumatları

    Returns:
        Order: Yaradılmış sifariş
    """
    try:
        validated_items = OrderValidator.model_validate(items)
        await Order.create(**validated_items.dict())
        return validated_items
    except (ValidationError, OperationalError) as e:
        if isinstance(e, ValidationError):
            logger.error(f"Məlumatın dogrulanması zamanı xəta yarandı: {e}")
        elif isinstance(e, OperationalError):
            logger.error(f"Database də işləmə zamanı xəta yarandı: {e}")
        else:
            logger.error(
                f"Bu xətanın niyə baş verdiyi haqqında heç bir fikrim yoxdu: {e}"
            )


@app.get("/all_users")
async def get_all_users():
    """Bütün istifadəçilərə baxmaq üçün
    Returns:
        List[User]: Bütün istifadəçilər
    """
    try:
        await User.all()
    except (OperationalError, DoesNotExist) as e:
        if isinstance(e, OperationalError):
            logger.error(f"Database də işləmə zamanı xəta yarandı: {e}")
        if isinstance(e, DoesNotExist):
            logger.error(f"Yalnış query ,istifadəçilər tapılmadı: {e}")
        else:
            logger.error(
                f"Bu xətanın niyə baş verdiyi haqqında heç bir fikrim yoxdu: {e}"
            )


@app.get("/all_orders")
async def get_all_orders():
    """Bütün sifarişlərə baxmaq üçün
    Returns:
        List[Order]: Bütün sifarişlər
    """
    try:
        await Order.all()
    except (OperationalError, DoesNotExist) as e:
        if isinstance(e, OperationalError):
            logger.error(f"Database də işləmə zamanı xəta yarandı: {e}")
        if isinstance(e, DoesNotExist):
            logger.error(f"Yalnış query ,sifarişlər tapılmadı: {e}")
        else:
            logger.error(
                f"Bu xətanın niyə baş verdiyi haqqında heç bir fikrim yoxdu: {e}"
            )


@app.on_event("shutdown")
async def close_connection():
    """Bağlantını bağlamaq üçün"""
    try:
        await close_db()
    except DBConnectionError as e:
        if isinstance(e, DBConnectionError):
            logger.error(f"Bağlantı bağlanmadı: {e}")
