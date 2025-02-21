import flet as ft
import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.Cliente import Cliente
colorLetra = ft.Colors.WHITE
colorInputLetra = ft.Colors.WHITE
colorFondo = ft.Colors.PINK_600


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    titulo = ft.Text("Estacionamiento", size=25, weight=ft.FontWeight.BOLD)
    clienteNombre = ft.TextField(
        label=ft.Text("Nombre Cliente", color=colorInputLetra),
        text_size=13,
        height=40,
        width=200,
        color=colorInputLetra,
    )
    telefono = ft.TextField(
        label=ft.Text("Telefono Cliente", color=colorInputLetra),
        text_size=13,
        height=40,
        width=200,
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
        width=200,
        color=colorInputLetra,
    )
    color = ft.TextField(
        label=ft.Text("Ingrese Color", color=colorInputLetra),
        text_size=13,
        height=40,
        width=200,
        color=colorInputLetra,
    )
    modelo = ft.TextField(
        label=ft.Text("Ingrese Modelo", color=colorInputLetra),
        text_size=13,
        height=40,
        width=200,
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
        ],
        [
            "José Martínez",
            "331655656",
            "sucre",
            "2024-02-20 12:00",
            "2024-02-20 20:00",
            "Moto",
            "$5",
            "Pagar",
        ],
        [
            "Laura Pérez",
            "331655656",
            "sucre",
            "2024-02-20 13:00",
            "2024-02-20 21:00",
            "Carro",
            "$10",
            "Pagar",
        ],
        [
            "Carlos Sánchez",
            "331655656",
            "sucre",
            "2024-02-20 14:00",
            "2024-02-20 22:00",
            "Moto",
            "$5",
            "Pagar",
        ],
        [
            "Sofía Ramírez",
            "331655656",
            "sucre",
            "2024-02-20 15:00",
            "2024-02-20 23:00",
            "Carro",
            "$10",
            "Pagar",
        ],
        [
            "Jorge Torres",
            "331655656",
            "sucre",
            "2024-02-20 16:00",
            "2024-02-20 00:00",
            "Moto",
            "$5",
            "Pagar",
        ],
        [
            "Patricia Gómez",
            "331655656",
            "sucre",
            "2024-02-20 17:00",
            "2024-02-20 01:00",
            "Carro",
            "$10",
            "Pagar",
        ],
        [
            "Daniel Vargas",
            "331655656",
            "sucre",
            "2024-02-20 18:00",
            "2024-02-20 02:00",
            "Moto",
            "$5",
            "Pagar",
        ],
        [
            "Rosa Mendoza",
            "331655656",
            "sucre",
            "2024-02-20 19:00",
            "2024-02-20 03:00",
            "Carro",
            "$10",
            "Pagar",
        ],
        [
            "Alberto Silva",
            "331655656",
            "sucre",
            "2024-02-20 20:00",
            "2024-02-20 04:00",
            "Moto",
            "$5",
            "Pagar",
        ],
        [
            "Elena Ortega",
            "331655656",
            "sucre",
            "2024-02-20 21:00",
            "2024-02-20 05:00",
            "Carro",
            "$10",
            "Pagar",
        ],
        [
            "Luis Núñez",
            "331655656",
            "sucre",
            "2024-02-20 22:00",
            "2024-02-20 06:00",
            "Moto",
            "$5",
            "Pagar",
        ],
        [
            "Carmen Guerrero",
            "331655656",
            "sucre",
            "2024-02-20 23:00",
            "2024-02-20 07:00",
            "Carro",
            "$10",
            "Pagar",
        ],
    ]

    # Agregar filas a la tabla dinámicamente
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
                            datos[fila][7],
                            on_click=lambda e: print(f"Pagar a {datos[fila][0]}"),
                        )
                    ),
                ]
            )
        )

    def guardarD(e):
        print("ssssss")
        cli=Cliente(1, "franz", "caballero", "gmail")
        cli.agregar_vehiculo(clienteNombre.value)

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

    def handle_change(self, e):
        self.fechaTiempoparking.value = e.control.value.strftime("%Y-%m-%d")
        self.page.update()


ft.app(target=main)
