from sqlalchemy import Column, Integer, String, Enum
from Base import Base  # Импорт Base из base.py

# Модель для задач
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(Enum("Pending", "Running", "Completed", "Failed", name="task_status"), default="Pending")
    logs = Column(String, nullable=True)
    dependencies = Column(String, nullable=True)
