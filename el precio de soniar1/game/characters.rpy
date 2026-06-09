# Definiciones de personajes para referenciar desde los scripts de Ren'Py.
# Las imagenes quedan comentadas hasta que existan los assets correspondientes.


# Gabriel ---------------------------------------------------------------------

define gabriel = Character("Gabriel", color="#9ecbff")
define pensamiento = Character(
    "Gabriel",
    color="#9ecbff",
    what_italic=True,
    what_prefix="(",
    what_suffix=")",
)

# image gabriel normal = "characters/gabriel_normal.png"
# image gabriel serio = "characters/gabriel_serio.png"
# image gabriel cansado = "characters/gabriel_cansado.png"
# image side gabriel normal = "characters/side/gabriel_normal.png"


# Eva -------------------------------------------------------------------------

define eva = Character("Eva", color="#f2b8c6")

# image eva normal = "characters/eva_normal.png"
# image eva preocupada = "characters/eva_preocupada.png"
# image eva cansada = "characters/eva_cansada.png"
# image side eva normal = "characters/side/eva_normal.png"


# Lucas -----------------------------------------------------------------------

define lucas = Character("Lucas", color="#ffd27f")

# image lucas normal = "characters/lucas_normal.png"
# image lucas feliz = "characters/lucas_feliz.png"
# image lucas triste = "characters/lucas_triste.png"
# image side lucas normal = "characters/side/lucas_normal.png"


# Daniel ----------------------------------------------------------------------

define daniel = Character("Daniel", color="#ff9f80")

# image daniel normal = "characters/daniel_normal.png"
# image daniel serio = "characters/daniel_serio.png"
# image daniel molesto = "characters/daniel_molesto.png"
# image side daniel normal = "characters/side/daniel_normal.png"


# Vagabundo -------------------------------------------------------------------

define vagabundo = Character(
    "Vagabundo",
    color="#b8d8a8",
    what_slow_cps=25,
)

# image vagabundo normal = "characters/vagabundo_normal.png"
# image vagabundo misterioso = "characters/vagabundo_misterioso.png"
# image side vagabundo normal = "characters/side/vagabundo_normal.png"


# Vendedor --------------------------------------------------------------------

define vendedor = Character("Vendedor", color="#d6b4ff")

# image vendedor normal = "characters/vendedor_normal.png"
# image vendedor amable = "characters/vendedor_amable.png"
# image side vendedor normal = "characters/side/vendedor_normal.png"


# Voces auxiliares ------------------------------------------------------------

define narrador = Character(None)
define correo = Character("Correo", color="#a9d6e5", what_color="#cfefff")
define sistema = Character(None, what_italic=True, what_text_align=0.5)

# image bg oficina = "backgrounds/oficina.png"
# image bg calle_lluvia = "backgrounds/calle_lluvia.png"
# image bg cocina = "backgrounds/cocina.png"
# image bg habitacion = "backgrounds/habitacion.png"
