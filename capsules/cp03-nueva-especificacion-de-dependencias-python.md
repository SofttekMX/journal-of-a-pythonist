# Nueva especificación de dependencias en Python

_Cápsula #3, la PEP751 ofrece una nueva alternativa a la especificación de dependencias en Python._

Probablemente, si has trabajado con proyectos en Python, te será conocido el archivo "requirements.txt", que especifica las dependencias de un proyecto y cuya especificación la podemos encontrar en la [PEP508](https://peps.python.org/pep-0508/) (11-Nov-2015).

Sin embargo, "Todo fluye, todo cambia, nada permanece" (Heráclito) y en semanas recientes, se aprobó una nueva especificación, la [PEP751](https://peps.python.org/pep-0751/) (31-Mar-2025).

> This PEP proposes a new file format (pyproject.toml) for specifying dependencies to enable reproducible installation in a Python environment. The format is designed to be human-readable and machine-generated. Installers consuming the file should be able to calculate what to install without the need for dependency resolution at install-time.
>
> _Paul Moore, CPython Core Developer_

Anteriormente, la [PEP665](https://peps.python.org/pep-0665/) buscaba actualizar la especificación PEP508, pero fue rechazada entre otros cosas, por observa que era necesario un mayor entendimiento de las necesidades en la comunidad:

> we definitely need a lockfile format that’s better than the current “pinned requirements file” approach, but I think we need a better understanding as a community of what we actually want in terms of functionality.
>
> _Paul Moore, CPython Core Developer_

Esta nueva especificación, la PEP751 ayuda a homologar las funcionalidades que herramientas como [pip-tools](https://pypi.org/project/pip-tools/), [pdm](https://pypi.org/project/pdm/), [poetry](https://python-poetry.org/) y [uv](https://docs.astral.sh/uv/) ya nos ofrecen como desarrolladores; como gestión de multiples ambientes, dependencias por entorno, etc.

_¿Conoces alguna de ellas…?_

- - -
