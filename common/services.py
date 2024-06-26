from typing import Any, Optional

from django.db.models import Model


def update_instance(
    *, instance: Model, data: dict[str, Any], fields: Optional[tuple[str, ...]] = None
) -> tuple[Model, bool]:
    is_updated = False

    if fields is None:
        fields = data.keys()

    for field in fields:
        if field not in data or not hasattr(instance, field) or getattr(instance, field) == data[field]:
            continue
        is_updated = True
        setattr(instance, field, data[field])

    if is_updated:
        instance.save()

    return instance, is_updated
