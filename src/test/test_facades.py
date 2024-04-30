from facades.users_facade import *
from facades.vacations_facade import *
from facades.likes_facade import *
from facades.countries_facade import *
from facades.roles_facade import *

### do try and except ###

with UsersFacade() as users_facade:
    pass

with VacationsFacade() as vacation_facade:
    pass

with LikesFacade() as likes_facade:
    pass

with CountriesFacade() as countries_facade:
    pass

with RolesFacade() as roles_facade:
    pass