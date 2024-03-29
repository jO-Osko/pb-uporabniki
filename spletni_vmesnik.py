import bottle
import model

@bottle.get("/")
def glavna_stran():
    # Stvari v GET pridejo v query
    od = int(bottle.request.query.get("od", 0))
    do = int(bottle.request.query.get("do", 1000))
    
    # Poberi vse uporabnike iz baze
    uporabniki = model.Uporabnik.dobi_uporabnike_med_idji(od, do)
    # Kaj naredimo z njimi -> Trenutno ne rabimo 0
    print(uporabniki)
    # Jih prikažemo
    return bottle.template("glavna.html", uporabniki=uporabniki,
                           od=od, do=do)

@bottle.get("/uporabniki/<uid:int>")
def uporabnik_detajli(uid):
    uporabnik = model.Uporabnik.dobi_uporabnika_z_idjem(uid)
    
    
    return bottle.template("detajl_uporabnika.html", 
                           uporabnik=uporabnik,
                           vsi_uporabniki=model.Uporabnik.dobi_vse_uporabnike())

@bottle.post("/uporabniki/<uid:int>")
def uporabnik_uredi_detajli(uid):
    uporabnik = model.Uporabnik.dobi_uporabnika_z_idjem(uid)
        
    novo_polno_ime = bottle.request.forms.getunicode("polno_ime")
    nov_email = bottle.request.forms.getunicode("email")
    
    uporabnik.polno_ime = novo_polno_ime
    uporabnik.email = nov_email
    
    uporabnik.shrani_v_bazo()
    
    bottle.redirect(f"/uporabniki/{uporabnik.uid}")


bottle.run(debug=True, reloader=True)
