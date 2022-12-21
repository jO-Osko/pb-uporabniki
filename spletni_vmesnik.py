import bottle
import model

@bottle.get("/")
def glavna_stran():
    return "Pozdravljen na glavni strani"

bottle.run(debug=True, reloader=True)