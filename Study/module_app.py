from package import withdraw
from package.deposit import deposit_current
import package.fd_rd
from package.fd_rd import rd

print(withdraw.withdraw_savings())
print(deposit_current())
print(package.fd_rd.fd())
print(rd())