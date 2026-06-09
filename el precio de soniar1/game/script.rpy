
label start:

    scene black

    narrador "DÍA 1"
    # TODO Arte: reemplazar por fondo pertinente.
    narrador "Fondo: Oficina gris, luz fluorescente parpadeante. Sonido de teclados y teléfonos de fondo."
    narrador "Se observa a Gabriel, sentado frente a la PC en su cubículo de la oficina."
    narrador "(Se abre una ventana emergente en la pantalla de la PC: un correo electrónico.)"

    call screen correo_convocatoria

    pensamiento "Faltan siete días. Solo siete días."

    narrador "(Entra Daniel, el jefe, caminando con paso pesado. Se apoya en el escritorio de Gabriel, invadiendo su espacio.)"

    daniel "Gabi, querido. Escuchame, surgió un problema con la carga de los remitos de la zona sur. Necesito que te quedes un par de horas más para cerrar el balance hoy."
    gabriel "Pero Daniel, hoy tenía que..."
    daniel "Dale, no me falles. Sabés que la mano viene dura y necesito gente comprometida. ¿Te quedás, no?"


    menu:
        "Aceptar":
            narrador "Gabriel acepta quedarse."
            jump dia1_parada_colectivo

        "Excusarse":
            narrador "Gabriel intenta excusarse."

    return

label dia1_parada_colectivo:

    "Gabriel asiente en silencio. Daniel le da una palmada condescendiente en el hombro y se va."

    "Se enfoca el reloj que transiciona de 18hs a 21hs."

    "Parada de colectivo. Noche. Lluvia. Gabriel está solo, encorvado bajo el frío. Un vagabundo sentado sobre unos cartones extiende una mano."

    vagabundo "Una ayuda, jefe... para un café. Hace mucho frío."

    menu:
        "Ayudarlo":
            jump casa_ayuda
        "Ignorarlo":
            jump casa_ignora

label casa_ayuda:

    "Gabriel saca un billete de 2.000 pesos arrugado. Se lo entrega al hombre."

    vagabundo "Gracias, bendiciones. Ya me ignoraron tantos que solo me quedaba soñar."

    gabriel "Mal día. Mañana será otro."

    vagabundo "Eso decimos todos. Tené cuidado, a veces uno se pasa la vida escribiendo el prólogo y se olvida de que el libro tiene muchas páginas."

    gabriel "¿Qué? ¿Vos sabés quién soy? ¿Cómo sabés que escribo?"

    vagabundo "Te aferrás a tus cosas como si tu vida estuviera ahí. Si llevas algo que vale la pena, lo abrazas."

    gabriel "Ya llega el bondi. Me tengo que ir."

    "Llega el colectivo. Gabriel sube rápido, pero se queda mirando por la ventanilla mientras el hombre vuelve a fundirse en la oscuridad."

    gabriel "{i}Uno se pasa la vida escribiendo el prólogo. Solo yo me encuentro estos personajes.{/i}"

    "Cocina pequeña, luz cálida pero tenue. Eva está lavando un plato. Lucas no está en escena."

    eva "Lucas ya se durmió. Estuvo preguntando por qué su papá no llegaba."

    gabriel "Perdón Eva. Daniel me encajó lo de zona sur. Me tuve que quedar."

    eva "¿Te van a pagar esta vez las horas extra? ¿O es otro favor para cuidar el puesto?"

    gabriel "Probablemente no... pero no puedo decir que no ahora. No con cómo están las cosas."

    "Se enfoca a Eva que suspira en resignación. Vuelve a Gabriel."

    gabriel "Eva, me queda una semana para terminar una historia. Si gano, puedo cambiar las cosas."

    eva "¿Ahora te parece el mejor momento, Gabriel? No sé si estamos para sueños ahora."

    "Eva sale de la cocina sin decir nada más. Se escucha el cierre de una puerta."

    "Habitación en penumbra. Solo la luz del monitor ilumina la cara de Gabriel. A un costado del teclado, se destaca el aviso de la AFIP."

call screen documento_aviso(
    "ARCA/AFIP - NOTIFICACIÓN DE DEUDA",
    "Se informa deuda pendiente. El expediente avanza a instancia de embargo preventivo.",
    "EMBARGO PREVENTIVO"
)

gabriel "{i}Tengo que escribir. Es lo único que me queda.{/i}"

menu:
        "Tono Melancólico":
            jump dia1_convergencia_final

        "Tono Cínico/Agresivo":
            jump dia1_convergencia_final

        "Tono Esperanzador":
            jump dia1_convergencia_final


label casa_ignora:

    "Gabriel da un paso atrás para evitar cruzar miradas con el hombre, acercándose demasiado al cordón de la vereda."

    "Un taxi pasa a toda velocidad, pisando de lleno un bache gigante. Un chorro de agua sucia y barro empapa a Gabriel de pies a cabeza. El vagabundo ni se inmuta, solo se cubre con su cartón."

    "Llega el colectivo. Gabriel sube rápido, chorreando agua. La gente a su alrededor lo mira con desagrado y se aparta. Se sienta junto a la ventanilla mojada."

    gabriel "{i}Qué locura cómo estamos. La calle no perdona a nadie.{/i}"

    "Entrada de la casa. Luz apagada, ambiente en completo silencio."

    "Gabriel está empapado y el agua sucia gotea sobre el piso."

    gabriel "{i}Me tengo que sacar el barro antes de poner a lavar esto.{/i}"

    "Transición."

    "Baño pequeño y azulejos viejos. Luz blanca parpadeante. Gabriel está encorvado frente a la pileta, intentando limpiar el barro de su ropa bajo el chorro de agua fría."

    "En el reflejo del espejo se ve a Eva apareciendo en el marco de la puerta."

    eva "Gabriel... escuché la puerta y no venías a la cocina. ¿Qué te pasó?"

    gabriel "Un taxi. Agarró un pozo enorme en la avenida. No pasa nada, sale con agua."

    eva "Estás temblando, Gabi. Y llegaste tardísimo, Lucas te estuvo esperando para..."

    gabriel "¡Ya sé que llegué tarde, Eva! ¡Me tuve que quedar haciendo los remitos de mierda de Daniel y encima me pasa esto! ¡No me lo recuerdes!"

    eva "No me grites. Yo no tengo la culpa de que no te animes a decirle que no a tu jefe."

    gabriel "Todo esto es para nosotros. Si gano el concurso la semana que viene..."

    eva "Mirate, Gabriel. Estás lavando barro de tu única ropa decente en un baño congelado a las diez de la noche. Secate y andá a dormir, no quiero que Lucas te escuche gritar así."

    "Eva sale, dejándolo solo."

    "Gabriel se vuelve a mirar en el espejo salpicado: está empapado, sucio y derrotado."

    "Transición."

    "Habitación en penumbra. Solo la luz del monitor ilumina la cara de Gabriel. A un costado del teclado, se destaca el aviso de la AFIP."

    call screen documento_aviso(
    "ARCA/AFIP - NOTIFICACIÓN DE DEUDA",
    "Se informa deuda pendiente. El expediente avanza a instancia de embargo preventivo.",
    "EMBARGO PREVENTIVO"
)

    gabriel "{i}Tengo que escribir. Es lo único que me queda.{/i}"

    menu:
        "Tono de Ira":
            jump dia1_convergencia_final

        "Tono de Culpa":
            jump dia1_convergencia_final

        "Tono de Indiferencia":
            jump dia1_convergencia_final



    return

label dia1_convergencia_final:

    narrador "(Tras elegir el tono del libro, se ve a Gabriel que saca una moneda del bolsillo. Se escucha solo la lluvia y se ve la luz del monitor reflejada.)"
    narrador "(Se enfoca la moneda y lleva a un flashback.)"
    sistema "FLASHBACK"
    narrador "(Habitación de Lucas. Lucas tiene dos juguetes en la mano. La habitación está bien iluminada. Día soleado.)"

    lucas "Me quiero llevar uno para mostrarle a mis amigos hoy, pero no sé cuál llevar, pa."
    gabriel "(Sonriendo, saca una moneda del bolsillo). Te voy a enseñar un truco. Vamos a tirarla. Cara es el auto, ceca es el dragón."
    lucas "¡Pero eso es elegir a ver cuál tiene más suerte! ¡No me gusta!"
    gabriel "Ahí está el secreto. Tirala bien alto. En el momento en que la moneda esté en el aire, antes de que caiga, vas a sentir que hay una de las dos opciones que preferís que salga."
    lucas "¿Para qué tiro la moneda entonces?"
    gabriel "Porque no importa lo que diga la moneda, solo qué sentiste mientras volaba. Vamos a probar."

    narrador "(Gabriel tira la moneda en el aire. Cae ceca.)"
    lucas "¡Vamos! ¡Llevo el dragón!"
    narrador "(Lucas le da un abrazo a Gabriel. Se enfoca la moneda en el piso.)"
    sistema "Fin del FLASHBACK"
    narrador "(Se ve a Gabriel con la moneda en la mano. Escenario anterior.)"

    pensamiento "¿Qué es lo que realmente quiero? ¿Qué tengo que hacer?"

    narrador "(Gabriel lanza la moneda. El sonido del metal girando en el aire invade todo el ambiente, tapando el ruido de la lluvia. Gabriel atrapa la moneda con un golpe seco, cubriéndola con la otra palma sobre el escritorio.)"
    narrador "(Gabriel no mira el resultado. Se lo escucha suspirar.)"
    narrador "(Pantalla a negro.)"
    sistema "FIN DEL DÍA 1"

