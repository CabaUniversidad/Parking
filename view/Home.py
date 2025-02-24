import flet as ft
import datetime
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.Cliente import Cliente
from models.Auto import Auto
from models.Moto import Moto
from services.control import ControlEstacionamiento

colorLetra = ft.Colors.WHITE
colorInputLetra = ft.Colors.WHITE
colorFondo = ft.Colors.PINK_600

control = ControlEstacionamiento(capacidad=5, tarifa_auto=10, tarifa_moto=5)


def main(page: ft.Page):
    titulo = ft.Text("Estacionamiento", size=25, weight=ft.FontWeight.BOLD)
    clienteNombre = ft.TextField(
        label=ft.Text("Nombre Cliente", color=colorInputLetra),
        text_size=13,
        height=40,
        width=200,
        color=colorInputLetra,
    )

    clienteApellido = ft.TextField(
        label=ft.Text("Apellido", color=colorInputLetra),
        text_size=13,
        height=40,
        width=200,
        color=colorInputLetra,
    )
    telefono = ft.TextField(
        label=ft.Text("Telefono Cliente", color=colorInputLetra),
        text_size=13,
        height=40,
        width=150,
        color=colorInputLetra,
    )
    direccion = ft.TextField(
        label=ft.Text("Direccion Cliente", color=colorInputLetra),
        text_size=13,
        height=40,
        width=200,
        color=colorInputLetra,
    )
    precio = ft.TextField(
        label=ft.Text("Precio", color=colorInputLetra),
        text_size=13,
        height=40,
        width=200,
        color=colorInputLetra,
    )
    TipoAutomovil = ft.Dropdown(
        text_size=13,
        height=40,
        width=150,
        label=ft.Text("Tipo de Automovil", color="white"),  # Cambia el color aquí
        color="white",
        options=[
            ft.dropdown.Option("Auto", text_style=ft.TextStyle(color=colorFondo)),
            ft.dropdown.Option("Moto", text_style=ft.TextStyle(color=colorFondo)),
            ft.dropdown.Option("Otro", text_style=ft.TextStyle(color=colorFondo)),
        ],
    )
    fechaTiempoparking = ft.Text("00/00/00", color=colorInputLetra)
    fechaActualPar = ft.Text("00/00/00", color=colorInputLetra)
    fechaActualPar.value = datetime.datetime.now().strftime("%Y-%m-%d")
    crFecha = ft.Row(
        controls=[
            fechaTiempoparking,
            ft.IconButton(
                icon=ft.Icons.CALENDAR_MONTH,
                style=ft.ButtonStyle(
                    bgcolor=colorLetra,
                ),
                on_click=lambda e: page.open(
                    ft.DatePicker(
                        first_date=datetime.datetime(year=2023, month=10, day=1),
                        last_date=datetime.datetime(
                            year=datetime.datetime.now().year, month=12, day=31
                        ),
                        on_change=handle_change,
                    )
                ),
            ),
        ]
    )
    placa = ft.TextField(
        label=ft.Text("Ingrese Placa", color=colorInputLetra),
        text_size=13,
        height=40,
        width=130,
        color=colorInputLetra,
    )
    marca = ft.TextField(
        label=ft.Text("Ingrese marca", color=colorInputLetra),
        text_size=13,
        height=40,
        width=130,
        color=colorInputLetra,
    )
    color = ft.TextField(
        label=ft.Text("Ingrese Color", color=colorInputLetra),
        text_size=13,
        height=40,
        width=130,
        color=colorInputLetra,
    )
    modelo = ft.TextField(
        label=ft.Text("Ingrese Modelo", color=colorInputLetra),
        text_size=13,
        height=40,
        width=130,
        color=colorInputLetra,
    )
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("telefono")),
            ft.DataColumn(ft.Text("Direccion")),
            ft.DataColumn(ft.Text("Fecha Llegada")),
            ft.DataColumn(ft.Text("Fecha Salida")),
            ft.DataColumn(ft.Text("tipo Vehiculo")),
            ft.DataColumn(ft.Text("Cobro")),
            ft.DataColumn(ft.Text("Acciones")),
        ],
        border=ft.border.all(1, ft.Colors.PINK_600),
        border_radius=15,
    )
    datos = [
        [
            "Ana López",
            "331655656",
            "sucre",
            "2024-02-20 09:30",
            "2024-02-20 17:45",
            "Moto",
            "$5",
            "Pagar",
        ],
        [
            "Juan González",
            "331655656,",
            "sucre",
            "2024-02-20 10:00",
            "2024-02-20 18:00",
            "Carro",
            "$10",
            "Pagar",
        ],
        [
            "María Rodríguez",
            "331655656",
            "sucre",
            "2024-02-20 11:00",
            "2024-02-20 19:00",
            "Carro",
            "$10",
            "Pagar",
        ]
    ]

    for fila in range(len(datos)):
        tabla.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(datos[fila][0])),
                    ft.DataCell(ft.Text(datos[fila][1])),
                    ft.DataCell(ft.Text(datos[fila][2])),
                    ft.DataCell(ft.Text(datos[fila][3])),
                    ft.DataCell(ft.Text(datos[fila][4])),
                    ft.DataCell(ft.Text(datos[fila][5])),
                    ft.DataCell(ft.Text(datos[fila][6])),
                    ft.DataCell(
                        ft.ElevatedButton(
                            "Detalle",
                            on_click=lambda e: print(f"Pagar a {datos[fila][0]}"),
                        )
                    ),
                ]
            )
        )

    def verificarEntrada():
        if not clienteNombre.value.strip():
            print("Error: El nombre del cliente es obligatorio.")
            return False
        if not clienteApellido.value.strip():
            print("Error: El apellido del cliente es obligatorio.")
            return False
        if not telefono.value.strip():
            print("Error: El teléfono del cliente es obligatorio.")
            return False
        if not direccion.value.strip():
            print("Error: La dirección del cliente es obligatoria.")
            return False
        if not precio.value.strip():
            print("Error: El precio es obligatorio.")
            return False
        if not TipoAutomovil.value:
            print("Error: Debe seleccionar un tipo de automóvil.")
            return False
        if not placa.value.strip():
            print("Error: La placa del vehículo es obligatoria.")
            return False
        if not marca.value.strip():
            print("Error: La marca del vehículo es obligatoria.")
            return False
        if not color.value.strip():
            print("Error: El color del vehículo es obligatorio.")
            return False
        if not modelo.value.strip():
            print("Error: El modelo del vehículo es obligatorio.")
            return False

        # Verificación de formato numérico en teléfono y precio
        if not telefono.value.isdigit():
            print("Error: El teléfono debe contener solo números.")
            return False
        """try:
            float(precio.value)  # Intentar convertir el precio a número
        except ValueError:
            print("Error: El precio debe ser un número válido.")
            return False

        print("✅ Todos los campos son válidos.")"""
        return True

    def guardarD(e):
        if not verificarEntrada():
            pass
        else:
            print("ssssss")
            cli = Cliente(
                1,
                clienteNombre.value,
                clienteApellido.value,
                telefono.value,
                direccion.value,
            )
            auto1 = Auto(placa.value, color.value, marca.value, modelo.value, 4)
            cli.agregar_vehiculo(auto1)
            control.estacionar(cli)
            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(clienteNombre.value)
                        ),
                        ft.DataCell(
                            ft.Text(telefono.value),
                        ),
                        ft.DataCell(
                            ft.Text(direccion.value),
                        ),
                        ft.DataCell(
                            ft.Text(fechaActualPar.value),
                        ),
                        ft.DataCell(
                            ft.Text(fechaTiempoparking.value)
                        ),
                        ft.DataCell(
                            ft.Text(TipoAutomovil.value)
                        ),
                        ft.DataCell(
                            ft.Text('5')
                        ),ft.DataCell(
                        ft.ElevatedButton(
                            "Detalle",
                            on_click=lambda e: print(f"Pagar a {clienteNombre.value}"),
                        )
                    ),
                    ]
                )
            )
        page.update()

    contenido = ft.Container(
        expand=True,
        content=ft.Column(
            controls=[
                ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[titulo]),
                ft.Divider(thickness=2),
                ft.Row(
                    height=200,
                    controls=[
                        ft.Container(
                            border_radius=8,
                            expand=True,
                            content=ft.Column(
                                controls=[
                                    ft.Container(
                                        padding=5,
                                        border_radius=8,
                                        expand=True,
                                        bgcolor=colorFondo,
                                        content=ft.Row(
                                            expand=True,
                                            controls=[
                                                ft.Column(
                                                    controls=[
                                                        ft.Text(
                                                            "Datos Cliente",
                                                            size=15,
                                                            weight=ft.FontWeight.BOLD,
                                                            color=colorLetra,
                                                        ),
                                                        ft.Row(
                                                            controls=[
                                                                clienteNombre,
                                                                clienteApellido,
                                                                telefono,
                                                                direccion,
                                                            ]
                                                        ),
                                                    ]
                                                )
                                            ],
                                        ),
                                    ),
                                    ft.Container(
                                        padding=5,
                                        border_radius=8,
                                        expand=True,
                                        bgcolor=colorFondo,
                                        content=ft.Row(
                                            expand=True,
                                            controls=[
                                                ft.Column(
                                                    controls=[
                                                        ft.Text(
                                                            "Datos Automovil",
                                                            size=15,
                                                            weight=ft.FontWeight.BOLD,
                                                            color=colorLetra,
                                                        ),
                                                        ft.Row(
                                                            controls=[
                                                                placa,
                                                                marca,
                                                                color,
                                                                modelo,
                                                                TipoAutomovil,
                                                            ]
                                                        ),
                                                    ]
                                                ),
                                            ],
                                        ),
                                    ),
                                ]
                            ),
                        ),
                        ft.Container(
                            padding=5,
                            border_radius=8,
                            width=400,
                            bgcolor=colorFondo,
                            content=ft.Column(
                                controls=[
                                    ft.Text(
                                        "Datos Parkeo",
                                        size=15,
                                        weight=ft.FontWeight.BOLD,
                                        color=colorLetra,
                                    ),
                                    ft.Divider(thickness=2),
                                    ft.Row(
                                        controls=[
                                            ft.Text(
                                                "Fecha de inicio",
                                                size=13,
                                                weight=ft.FontWeight.BOLD,
                                                color=colorLetra,
                                            ),
                                            fechaActualPar,
                                        ]
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Text(
                                                "Fecha de Salida",
                                                size=13,
                                                weight=ft.FontWeight.BOLD,
                                                color=colorLetra,
                                            ),
                                            crFecha,
                                        ]
                                    ),
                                    ft.Row(
                                        controls=[
                                            precio,
                                            ft.TextButton(
                                                "guardar",
                                                icon=ft.icons.SAVE,
                                                style=ft.ButtonStyle(
                                                    bgcolor=colorLetra,
                                                ),
                                                on_click=guardarD,
                                            ),
                                        ]
                                    ),
                                ]
                            ),
                        ),
                    ],
                ),
                ft.Container(
                    expand=True,
                    border_radius=10,
                    padding=5,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        expand=True,
                        controls=[
                            ft.Container(
                                height=400,
                                content=ft.Column(
                                    scroll=ft.ScrollMode.AUTO,
                                    controls=[
                                        tabla,
                                    ],
                                ),
                            )
                        ],
                    ),
                ),
            ],
        ),
    )
    page.add(contenido)

    def handle_change(e):
        fechaTiempoparking.value = e.control.value.strftime("%Y-%m-%d")
        page.update()
