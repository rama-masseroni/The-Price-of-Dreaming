# Definiciones de personajes e imagenes para los dialogos de Ren'Py.


# Posiciones reutilizables para mostrar dos bustos en una misma escena.
transform busto_izquierda:
    xalign 0.0
    yalign 0.5

transform busto_derecha:
    xalign 1.0
    yalign 0.5


init python:
    def busto_con_sombra(path):
        size = 700
        padding = 20
        canvas_size = size + padding * 2

        busto = Transform(path, xysize=(size, size))
        busto_con_margen = Composite(
            (canvas_size, canvas_size),
            (padding, padding), busto,
        )
        sombra = Transform(
            busto_con_margen,
            matrixcolor=TintMatrix("#000000"),
            alpha=0.95,
            xoffset=14,
        )

        return Fixed(
            sombra,
            busto_con_margen,
            xysize=(canvas_size, canvas_size),
        )


# Gabriel ---------------------------------------------------------------------

define gabriel = Character("Gabriel", color="#24527a", image="gabriel")
define pensamiento = Character(
    "Gabriel",
    color="#24527a",
    image="gabriel",
    what_italic=True,
    what_prefix="(",
    what_suffix=")",
)

image gabriel normal = busto_con_sombra("art/faces/gabriel_normal.png")
image gabriel feliz = busto_con_sombra("art/faces/gabriel_feliz.png")
image gabriel enojado = busto_con_sombra("art/faces/gabriel_enojado.png")
image gabriel triste = busto_con_sombra("art/faces/gabriel_triste.png")
image side gabriel = im.Scale("art/faces/gabriel_normal.png", 700, 700)
image side gabriel normal = im.Scale("art/faces/gabriel_normal.png", 700, 700)
image side gabriel feliz = im.Scale("art/faces/gabriel_feliz.png", 700, 700)
image side gabriel enojado = im.Scale("art/faces/gabriel_enojado.png", 700, 700)
image side gabriel triste = im.Scale("art/faces/gabriel_triste.png", 700, 700)


# Eva -------------------------------------------------------------------------

define eva = Character("Eva", color="#7a3045", image="eva")

image eva normal = busto_con_sombra("art/faces/eva_normal.png")
image eva feliz = busto_con_sombra("art/faces/eva_feliz.png")
image eva enojada = busto_con_sombra("art/faces/eva_enojada.png")
image eva triste = busto_con_sombra("art/faces/eva_triste.png")
image side eva = im.Scale("art/faces/eva_normal.png", 700, 700)
image side eva normal = im.Scale("art/faces/eva_normal.png", 700, 700)
image side eva feliz = im.Scale("art/faces/eva_feliz.png", 700, 700)
image side eva enojada = im.Scale("art/faces/eva_enojada.png", 700, 700)
image side eva triste = im.Scale("art/faces/eva_triste.png", 700, 700)


# Lucas -----------------------------------------------------------------------

define lucas = Character("Lucas", color="#805610", image="lucas")

image lucas normal = busto_con_sombra("art/faces/lucas_normal.png")
image lucas feliz = busto_con_sombra("art/faces/lucas_feliz.png")
image lucas enojado = busto_con_sombra("art/faces/lucas_enojado.png")
image lucas triste = busto_con_sombra("art/faces/lucas_triste.png")
image side lucas = im.Scale("art/faces/lucas_normal.png", 700, 700)
image side lucas normal = im.Scale("art/faces/lucas_normal.png", 700, 700)
image side lucas feliz = im.Scale("art/faces/lucas_feliz.png", 700, 700)
image side lucas enojado = im.Scale("art/faces/lucas_enojado.png", 700, 700)
image side lucas triste = im.Scale("art/faces/lucas_triste.png", 700, 700)


# Daniel ----------------------------------------------------------------------

define daniel = Character("Daniel", color="#8a3425", image="daniel")

image daniel normal = busto_con_sombra("art/faces/daniel_normal.png")
image daniel enojado = busto_con_sombra("art/faces/daniel_enojado.png")
image side daniel = im.Scale("art/faces/daniel_normal.png", 700, 700)
image side daniel normal = im.Scale("art/faces/daniel_normal.png", 700, 700)
image side daniel enojado = im.Scale("art/faces/daniel_enojado.png", 700, 700)


# Vagabundo -------------------------------------------------------------------

define vagabundo = Character(
    "Vagabundo",
    color="#3f6634",
    image="vagabundo",
    what_slow_cps=25,
)

image vagabundo normal = busto_con_sombra("art/faces/vagabundo_normal.png")
image vagabundo feliz = busto_con_sombra("art/faces/vagabundo_feliz.png")
image vagabundo enojado = busto_con_sombra("art/faces/vagabundo_enojado.png")
image side vagabundo = im.Scale("art/faces/vagabundo_normal.png", 700, 700)
image side vagabundo normal = im.Scale("art/faces/vagabundo_normal.png", 700, 700)
image side vagabundo feliz = im.Scale("art/faces/vagabundo_feliz.png", 700, 700)
image side vagabundo enojado = im.Scale("art/faces/vagabundo_enojado.png", 700, 700)


# Vendedor --------------------------------------------------------------------

define vendedor = Character("Vendedor", color="#59347d", image="vendedor")

image vendedor normal = busto_con_sombra("art/faces/vendedor_normal.png")
image vendedor feliz = busto_con_sombra("art/faces/vendedor_feliz.png")
image side vendedor = im.Scale("art/faces/vendedor_normal.png", 700, 700)
image side vendedor normal = im.Scale("art/faces/vendedor_normal.png", 700, 700)
image side vendedor feliz = im.Scale("art/faces/vendedor_feliz.png", 700, 700)


# Voces auxiliares ------------------------------------------------------------

define narrador = Character(None)
define correo = Character("Correo", color="#2d5e70", what_color="#cfefff")
define sistema = Character(None, what_italic=True, what_text_align=0.5)
