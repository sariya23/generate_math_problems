from common.bounds import Bounds


def get_bounds_for_generated_constants(joined_bounds: str) -> Bounds:
    """
    Метод преобразует граничные значения для констант из
    формы a, b в удобную форму для передачи генерирующим функциям.
    """
    start, end = joined_bounds.split(',')
    return Bounds(
        start_value=int(start),
        end_value=int(end),
    )