from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ('created_at', 'updated_at'):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            # Set id and created_at for new instance as previously done
            # This is just a placeholder; adjust with your actual implementation
            self.id = "Generate new id here"
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
