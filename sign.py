<<<<<<< HEAD
# Crea la función sign()
def sign(x):
    """Devuelve el signo de número."""
    if x == None:
        return None
    if x < 0:
        return -1

# Prueba la función sign()
def test_sign():
    assert sign(-10) == -1
    assert sign(10) == 1
    assert sign(0) == 1
    assert sign(None) == None
=======
# Crea la función sign()
def sign(x):
    """Devuelve el signo de número."""
    if x == None:
        return None
    if x < 0:
        return -1

# Prueba la función sign()
def test_sign():
    assert sign(-10) == -1
    assert sign(10) == 1
    assert sign(0) == 1
    assert sign(None) == None
>>>>>>> ab8afeb48b00a5afa9bc7c3905aa6adf0834859f
