# Calculadora de Gastos

Aplicación de consola en Python para registrar gastos, ver el total acumulado y filtrar por categoría.

## Requisitos

Python 3.10 o superior (se usa `match`/`case`).

## Características

- Añadir gastos con validación (descripción, importe mayor que cero, categoría).
- Listar todos los gastos registrados.
- Ver el total acumulado.
- Filtrar por categoría sin distinguir mayúsculas de minúsculas.

## Uso

```bash
python calculadora_gastos.py
```

## Estructura

- `agregar_gasto()`, `listar_gastos()`, `calcular_total()`, `filtrar_por_categoria()`: operaciones sobre la lista de gastos.
- `main()`: menú principal y validación de entradas.
