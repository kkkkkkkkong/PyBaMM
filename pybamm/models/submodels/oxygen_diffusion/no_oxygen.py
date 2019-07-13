#
# Class for when there is no oxygen
#
import pybamm

from .base_oxygen_diffusion import BaseModel


class NoOxygen(BaseModel):
    """Class for when there is no oxygen

    Parameters
    ----------
    param : parameter class
        The parameters to use for this submodel


    **Extends:** :class:`pybamm.oxygen_diffusion.BaseModel`
    """

    def __init__(self, param):
        super().__init__(param)

    def get_fundamental_variables(self):
        c_ox_n = pybamm.Broadcast(0, ["negative electrode"])
        c_ox_s = pybamm.Broadcast(0, ["separator"])
        c_ox_p = pybamm.Broadcast(0, ["positive electrode"])
        c_ox = pybamm.Concatenation(c_ox_n, c_ox_s, c_ox_p)

        variables = self._get_standard_concentration_variables(c_ox)

        N_e = pybamm.Broadcast(
            0, ["negative electrode", "separator", "positive electrode"]
        )

        variables.update(self._get_standard_flux_variables(N_e))

        return variables
