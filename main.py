from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import tablas, esquemas
from conexion import SessionLocal, engine


app = FastAPI()

# Dependencia para obtener sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


##Crear computador (POST)
@app.post("/computadores/", response_model=esquemas.ComputadorRespuesta)
def crear_computador(computador: esquemas.ComputadorBase, db: Session = Depends(get_db)):
    computador_existente = db.query(tablas.Computadores).filter(tablas.Computadores.referencia == computador.referencia).first()
    if computador_existente:
        raise HTTPException(status_code=400, detail="El computador ya existe")

    db_computador = tablas.Computadores(referencia = computador.referencia, marca = computador.marca, cpu = computador.cpu, ram = computador.ram, almacenamiento = computador.almacenamiento)
    db.add(db_computador)
    db.commit()
    db.refresh(db_computador)
    return db_computador


@app.get("/computadores/", response_model=list[esquemas.ComputadorRespuesta])
def consultar_computadores(db: Session = Depends(get_db)):
    return db.query(tablas.Computadores).all()


@app.get("/computadores/{referencia}", response_model=esquemas.ComputadorRespuesta)
def buscar_computador(referencia = str, db: Session = Depends(get_db)):
    computador = db.query(tablas.Computadores).filter(tablas.Computadores.referencia == referencia).first()
    if computador is None:
        raise HTTPException(status_code=404, detail="Referencia de PC no encontrada")
    else:
        return computador


@app.put("/computadores/{referencia}", response_model=esquemas.ComputadorRespuesta)
def actualizar_computador(computador_actualizado: esquemas.ComputadorBase, referencia = str, db: Session = Depends(get_db)):
    computador = db.query(tablas.Computadores).filter(tablas.Computadores.referencia == referencia).first()
    if computador is None:
        raise HTTPException(status_code=404, detail="Referencia de PC no encontrada")
    else:
        computador.marca = computador_actualizado.marca
        computador.ram = computador_actualizado.ram
        computador.cpu = computador_actualizado.cpu
        computador.almacenamiento = computador_actualizado.almacenamiento
        db.commit()
        db.refresh(computador)
        return computador


@app.delete("/computadores/{referencia}")
def eliminar_computador(referencia = str, db: Session = Depends(get_db)):
    computador = db.query(tablas.Computadores).filter(tablas.Computadores.referencia == referencia).first()
    if computador is None:
        raise HTTPException(status_code=404, detail="Referencia de PC no encontrada")
    else:
        db.delete(computador)
        db.commit()
        return {"mensaje": "Computador eliminado "}



##Crear Almacenamiento de computador
@app.post("/almacen/", response_model=esquemas.AlmacenRespuesta)
def crear_almacenaje(almacenaje: esquemas.AlmacenBase, db: Session = Depends(get_db)):
    ##GET interno para validar que exista la referencia de computador en la tabla computadores
    computador = db.query(tablas.Computadores).filter(tablas.Computadores.referencia == almacenaje.referencia_comp).first()
    if computador is None:
        raise HTTPException(status_code=404, detail="Referencia de PC no encontrada")
    almacen_existente = db.query(tablas.Almacen).filter(tablas.Almacen.referencia_comp == almacenaje.referencia_comp).first()
    if almacen_existente:
        raise HTTPException(status_code=404, detail="Ya existe un registro en el almacen para esta referencia")
    ##si existe la referencia de computador y aun no se encuentra creado el almacenaje en la tabla de almacen se procede a crear el registro
    db_almacen = tablas.Almacen(referencia_comp = almacenaje.referencia_comp, cantidad = almacenaje.cantidad)
    db.add(db_almacen)
    db.commit()
    db.refresh(db_almacen)
    return db_almacen


@app.get("/almacen/", response_model=list[esquemas.AlmacenRespuesta])
def consultar_almacen(db: Session = Depends(get_db)):
    return db.query(tablas.Almacen).all()


@app.get("/almacen/{referencia_comp}", response_model=esquemas.AlmacenRespuesta)
def buscar_almacenaje(referencia_comp = str, db: Session = Depends(get_db)):
    almacen = db.query(tablas.Almacen).filter(tablas.Almacen.referencia_comp == referencia_comp).first()
    if almacen is None:
        raise HTTPException(status_code=404, detail="No existe un registro en el almacen para esta referencia")
    else:
        return almacen


@app.put("/almacen/{referencia_comp}", response_model=esquemas.AlmacenRespuesta)
def actualizar_almacenaje(almacen_actualizado: esquemas.AlmacenBase, referencia_comp = str, db: Session = Depends(get_db)):
    almacen = db.query(tablas.Almacen).filter(tablas.Almacen.referencia_comp == referencia_comp).first()
    if almacen is None:
        raise HTTPException(status_code=404, detail="No existe un registro en el almacen para esta referencia")
    else:
        nueva_cantidad = almacen.cantidad + almacen_actualizado.cantidad
        almacen.cantidad = nueva_cantidad
        db.commit()
        db.refresh(almacen)
        return almacen


@app.delete("/almacen/{referencia_comp}")
def eliminar_almacen(referencia_comp = str, db: Session = Depends(get_db)):
    almacen = db.query(tablas.Almacen).filter(tablas.Almacen.referencia_comp == referencia_comp).first()
    if almacen is None:
        raise HTTPException(status_code=404, detail="No existe un registro en el almacen para esta referencia")
    else:
        db.delete(almacen)
        db.commit()
        return {"mensaje": "Almacenaje eliminado "}