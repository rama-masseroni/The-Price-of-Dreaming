# Definiciones de personajes e imagenes para los dialogos de Ren'Py.


# Posiciones reutilizables para mostrar dos bustos en una misma escena.
transform busto_izquierda:
    xalign 0.0
    yalign 0.5

transform busto_derecha:
    xalign 1.0
    yalign 0.5


# Gabriel ---------------------------------------------------------------------

define gabriel = Character("Gabriel", color="#9ecbff", image="gabriel")
define pensamiento = Character(
    "Gabriel",
    color="#9ecbff",
    image="gabriel",
    what_italic=True,
    what_prefix="(",
    what_suffix=")",
)

image gabriel normal = im.Scale("art/faces/gabriel_normal.png", 700, 700)
image gabriel feliz = im.Scale("art/faces/gabriel_feliz.png", 700, 700)
image gabriel enojado = im.Scale("art/faces/gabriel_enojado.png", 700, 700)
image side gabriel = im.Scale("art/faces/gabriel_normal.png", 700, 700)
image side gabriel normal = im.Scale("art/faces/gabriel_normal.png", 700, 700)
image side gabriel feliz = im.Scale("art/faces/gabriel_feliz.png", 700, 700)
image side gabriel enojado = im.Scale("art/faces/gabriel_enojado.png", 700, 700)


# Eva -------------------------------------------------------------------------

define eva = Character("Eva", color="#f2b8c6", image="eva")

image eva normal = im.Scale("art/faces/eva_normal.png", 700, 700)
image eva feliz = im.Scale("art/faces/eva_feliz.png", 700, 700)
image eva enojada = im.Scale("art/faces/eva_enojada.png", 700, 700)
image side eva = im.Scale("art/faces/eva_normal.png", 700, 700)
image side eva normal = im.Scale("art/faces/eva_normal.png", 700, 700)
image side eva feliz = im.Scale("art/faces/eva_feliz.png", 700, 700)
image side eva enojada = im.Scale("art/faces/eva_enojada.png", 700, 700)


# Lucas -----------------------------------------------------------------------

define lucas = Character("Lucas", color="#ffd27f", image="lucas")

image lucas normal = im.Scale("art/faces/lucas_normal.png", 700, 700)
image lucas feliz = im.Scale("art/faces/lucas_feliz.png", 700, 700)
image lucas enojado = im.Scale("art/faces/lucas_enojado.png", 700, 700)
image side lucas = im.Scale("art/faces/lucas_normal.png", 700, 700)
image side lucas normal = im.Scale("art/faces/lucas_normal.png", 700, 700)
image side lucas feliz = im.Scale("art/faces/lucas_feliz.png", 700, 700)
image side lucas enojado = im.Scale("art/faces/lucas_enojado.png", 700, 700)


# Daniel ----------------------------------------------------------------------

define daniel = Character("Daniel", color="#ff9f80", image="daniel")

image daniel normal = im.Scale("art/faces/daniel_normal.png", 700, 700)
image side daniel = im.Scale("art/faces/daniel_normal.png", 700, 700)
image side daniel normal = im.Scale("art/faces/daniel_normal.png", 700, 700)


# Vagabundo -------------------------------------------------------------------

define vagabundo = Character(
    "Vagabundo",
    color="#b8d8a8",
    image="vagabundo",
    what_slow_cps=25,
)

image vagabundo normal = im.Scale("art/faces/vagabundo_normal.png", 700, 700)
image side vagabundo = im.Scale("art/faces/vagabundo_normal.png", 700, 700)
image side vagabundo normal = im.Scale("art/faces/vagabundo_normal.png", 700, 700)


# Vendedor --------------------------------------------------------------------

define vendedor = Character("Vendedor", color="#d6b4ff", image="vendedor")

image vendedor normal = im.Scale("art/faces/vendedor_normal.png", 700, 700)
image side vendedor = im.Scale("art/faces/vendedor_normal.png", 700, 700)
image side vendedor normal = im.Scale("art/faces/vendedor_normal.png", 700, 700)


# Voces auxiliares ------------------------------------------------------------

define narrador = Character(None)
define correo = Character("Correo", color="#a9d6e5", what_color="#cfefff")
define sistema = Character(None, what_italic=True, what_text_align=0.5)
