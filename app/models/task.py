from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    completed_at = db.Column(db.DateTime, nullable=True)
    goal_id = db.Column(db.Integer, db.ForeignKey("goal.goal_id"), nullable=True)
    goal = db.relationship("Goal", back_populates="tasks")

    def to_dict(self):
        task_as_dict = {
            "id": self.task_id,
            "title": self.title,
            "description": self.description,
            "is_complete": bool(self.completed_at)
            }
        
        if self.goal_id:
            task_as_dict["goal_id"] = self.goal_id

        return task_as_dict
    @classmethod
    def from_dict(cls, task_data):
        if "completed_at" not in task_data:
            task_data["completed_at"] = None
        
        return Task(
            title=task_data["title"],
            description=task_data["description"],
            completed_at=task_data["completed_at"]
        )