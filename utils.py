def get_bounds_for_generated_constants(joined_bounds: str) -> tuple[int, int]:
    """
    Метод преобразует граничные значения для констант из
    формы a, b в удобную форму для передачи генерирующим функциям.
    """
    start, end = joined_bounds.split(',')
    return int(start), int(end)