from tkinter import *
from tkinter import ttk
from decimal import Decimal

window = Tk()
window.title('Unit converter')
window.geometry('640x180')
window.iconbitmap('./unit_converter.ico')

# ----------------------------------------------------------------------------------------

previous_unit_type_selection = unit_type_selection = 'Length'
from_unit = 'Kilometer'
to_unit = 'Mile'


# function calling from unit_select_action()
def set_options(unit_options, from_index, to_index):
    global previous_unit_type_selection
    from_drop.config(values=unit_options)
    from_drop.current(from_index)
    to_drop.config(values=unit_options)
    to_drop.current(to_index)
    previous_unit_type_selection = unit_type_selection


# from and to options are set according to unit type selections
def unit_select_action(_):
    global unit_type_selection
    from_value.set('1')
    unit_type_selection = unit_type_drop.get()
    if unit_type_selection != previous_unit_type_selection:
        if unit_type_selection == 'Length':
            set_options(length_options, 0, 1)
        elif unit_type_selection == 'Mass':
            set_options(mass_options, 1, 8)
        elif unit_type_selection == 'Time':
            set_options(time_options, 7, 6)
        elif unit_type_selection == 'Temperature':
            set_options(temp_options, 0, 2)
        elif unit_type_selection == 'Area':
            set_options(area_options, 0, 2)
        elif unit_type_selection == 'Data Transfer Rate':
            set_options(data_rate_options, 2, 3)
        elif unit_type_selection == 'Digital Storage':
            set_options(dig_store_options, 12, 14)
        elif unit_type_selection == 'Energy':
            set_options(energy_options, 6, 0)
        elif unit_type_selection == 'Frequency':
            set_options(freq_options, 1, 2)
        elif unit_type_selection == 'Fuel Economy':
            set_options(fuel_economy_options, 2, 3)
        elif unit_type_selection == 'Plane Angle':
            set_options(plane_angle_options, 0, 4)
        elif unit_type_selection == 'Pressure':
            set_options(pressure_options, 1, 3)
        elif unit_type_selection == 'Speed':
            set_options(speed_options, 0, 3)
        else:
            set_options(volume_options, 8, 7)


# ---------------------------------------------------------------------------------------
# swap button action
def swap_units():
    temp = to_drop.get()
    to_drop.set(from_drop.get())
    from_drop.set(temp)


# ---------------------------------------------------------------------------------------
def cleaning(result_string):
    if '.' not in result_string:
        return result_string
    else:
        if 'E' in result_string:
            e_index = result_string.index('E')
            e_value = result_string[e_index:]
            result_string = result_string[:e_index]
        else:
            e_value = ''
        point_index = result_string.index('.')
        integer_part = result_string[:point_index]
        fraction_part = result_string[point_index:]
        while fraction_part[-1] == '0' and len(fraction_part) != 1:
            fraction_part = fraction_part[:-1]
        if fraction_part == '.':
            return integer_part + e_value
        else:
            return integer_part + fraction_part[:9] + e_value


# ----------------------------------------------------------------------------------
def length_entry_changing(entry_value):
    global from_unit
    # if from_drop is Kilometer
    if from_unit == 'Kilometer':
        if to_unit == 'Kilometer':
            to_value.set(cleaning(entry_value))
        elif to_unit == 'Meter':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1000'))))
        elif to_unit == 'Centimeter':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1e+5'))))
        elif to_unit == 'Millimeter':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1e+6'))))
        elif to_unit == 'Micrometer':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1e+9'))))
        elif to_unit == 'Nanometer':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1e+12'))))
        elif to_unit == 'Picometer':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1e+15'))))
        elif to_unit == 'Mile':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('0.621371'))))
        elif to_unit == 'Yard':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1093.61'))))
        elif to_unit == 'Foot':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('3280.84'))))
        elif to_unit == 'Inch':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('39370.1'))))
        elif to_unit == 'Nautical mile':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('0.53995'))))
    else:  # if from drop is other than Kilometer, we first convert it to kilometer then to required unit
        if from_unit == 'Meter':
            entry_value = str(Decimal(entry_value) / Decimal('1000'))
        elif from_unit == 'Centimeter':
            entry_value = str(Decimal(entry_value) / Decimal('1e+5'))
        elif from_unit == 'Millimeter':
            entry_value = str(Decimal(entry_value) / Decimal('1e+6'))
        elif from_unit == 'Micrometer':
            entry_value = str(Decimal(entry_value) / Decimal('1e+9'))
        elif from_unit == 'Nanometer':
            entry_value = str(Decimal(entry_value) / Decimal('1e+12'))
        elif from_unit == 'Picometer':
            entry_value = str(Decimal(entry_value) / Decimal('1e+15'))
        elif from_unit == 'Mile':
            entry_value = str(Decimal(entry_value) / Decimal('0.621371'))
        elif from_unit == 'Yard':
            entry_value = str(Decimal(entry_value) / Decimal('1093.61'))
        elif from_unit == 'Foot':
            entry_value = str(Decimal(entry_value) / Decimal('3280.84'))
        elif from_unit == 'Inch':
            entry_value = str(Decimal(entry_value) / Decimal('39370.1'))
        else:
            entry_value = str(Decimal(entry_value) / Decimal('0.53995'))
        from_unit = 'Kilometer'
        length_entry_changing(entry_value)


def mass_entry_changing(entry_value):
    global from_unit
    # if from_drop is Kilogram
    if from_unit == 'Kilogram':
        if to_unit == 'tonne':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('0.001'))))
        elif to_unit == 'Kilogram':
            to_value.set(cleaning(entry_value))
        elif to_unit == 'Gram':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1000'))))
        elif to_unit == 'Milligram':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1e+6'))))
        elif to_unit == 'Microgram':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1e+9'))))
        elif to_unit == 'Imperial ton':
            to_value.set(cleaning(str(Decimal(entry_value) * (Decimal(1) / Decimal('1016.05')))))
        elif to_unit == 'US ton':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('0.00110231'))))
        elif to_unit == 'Stone':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('0.1574731'))))
        elif to_unit == 'Pound':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('2.20462'))))
        elif to_unit == 'Ounce':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('35.274'))))
    else:  # if from drop is other than Kilogram, we first convert it to Kilogram then to required unit
        if from_unit == 'tonne':
            entry_value = str(Decimal(entry_value) * Decimal('1000'))
        elif from_unit == 'Gram':
            entry_value = str(Decimal(entry_value) * Decimal('0.001'))
        elif from_unit == 'Milligram':
            entry_value = str(Decimal(entry_value) * Decimal('1e-6'))
        elif from_unit == 'Microgram':
            entry_value = str(Decimal(entry_value) * Decimal('1e-9'))
        elif from_unit == 'Imperial ton':
            entry_value = str(Decimal(entry_value) * Decimal('1016.05'))
        elif from_unit == 'US ton':
            entry_value = str(Decimal(entry_value) / Decimal('0.00110231'))
        elif from_unit == 'Stone':
            entry_value = str(Decimal(entry_value) / Decimal('0.1574731'))
        elif from_unit == 'Pound':
            entry_value = str(Decimal(entry_value) / Decimal('2.20462'))
        else:
            entry_value = str(Decimal(entry_value) / Decimal('35.274'))
        from_unit = 'Kilogram'
        mass_entry_changing(entry_value)


def time_entry_changing(entry_value):
    global from_unit
    # if from drop is Week
    if from_unit == 'Week':
        if to_unit == 'Nanosecond':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('6.048e+14'))))
        elif to_unit == 'Microsecond':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('6.048e+11'))))
        elif to_unit == 'Millisecond':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('6.048e+8'))))
        elif to_unit == 'Second':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('604800'))))
        elif to_unit == 'Minute':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('10080'))))
        elif to_unit == 'Hour':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('168'))))
        elif to_unit == 'Day':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('7'))))
        elif to_unit == 'Week':
            to_value.set(cleaning(entry_value))
        elif to_unit == 'Month':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('0.230137'))))
        elif to_unit == 'Calendar year':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('0.0191781'))))
        elif to_unit == 'Decade':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('0.00191781'))))
        elif to_unit == 'Century':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('0.000191781'))))
    else:  # if from drop is other than Week, we first convert it to Week then to required unit
        if from_unit == 'Nanosecond':
            entry_value = str(Decimal(entry_value) / Decimal('6.048e+14'))
        elif from_unit == 'Microsecond':
            entry_value = str(Decimal(entry_value) / Decimal('6.048e+11'))
        elif from_unit == 'Millisecond':
            entry_value = str(Decimal(entry_value) / Decimal('6.048e+8'))
        elif from_unit == 'Second':
            entry_value = str(Decimal(entry_value) / Decimal('604800'))
        elif from_unit == 'Minute':
            entry_value = str(Decimal(entry_value) / Decimal('10080'))
        elif from_unit == 'Hour':
            entry_value = str(Decimal(entry_value) / Decimal('168'))
        elif from_unit == 'Day':
            entry_value = str(Decimal(entry_value) / Decimal('7'))
        elif from_unit == 'Month':
            entry_value = str(Decimal(entry_value) / Decimal('0.230137'))
        elif from_unit == 'Calendar year':
            entry_value = str(Decimal(entry_value) / Decimal('0.0191781'))
        elif from_unit == 'Decade':
            entry_value = str(Decimal(entry_value) / Decimal('0.00191781'))
        else:
            entry_value = str(Decimal(entry_value) / Decimal('0.000191781'))
        from_unit = 'Week'
        time_entry_changing(entry_value)


def temp_entry_changing(entry_value):
    global from_unit
    # if from_drop is Celsius
    if from_unit == 'Celsius':
        if to_unit == 'Celsius':
            to_value.set(cleaning(entry_value))
        elif to_unit == 'Fahrenheit':
            to_value.set(cleaning(str(Decimal('32') + (Decimal(entry_value) * (Decimal('9') / Decimal('5'))))))
        elif to_unit == 'Kelvin':
            to_value.set(cleaning(str(Decimal(entry_value) + Decimal('273.15'))))
    else:  # if from drop is other than 'Celsius', we first convert it to it then to required unit
        if from_unit == 'Fahrenheit':
            entry_value = str((Decimal('5') / Decimal('9')) * (Decimal(entry_value) - Decimal('32')))
        else:
            entry_value = str(Decimal(entry_value) - Decimal('273.15'))
        from_unit = 'Celsius'
        temp_entry_changing(entry_value)


def area_entry_changing(entry_value):
    global from_unit
    # if from drop is Square kilometer
    if from_unit == 'square kilometer':
        if to_unit == 'square kilometer':
            to_value.set(cleaning(entry_value))
        elif to_unit == 'square meter':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1e+6'))))
        elif to_unit == 'square mile':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('0.386102'))))
        elif to_unit == 'square yard':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1.196e+6'))))
        elif to_unit == 'square foot':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1.076e+7'))))
        elif to_unit == 'square inch':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1.55e+9'))))
        elif to_unit == 'hectare':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('100'))))
        elif to_unit == 'acre':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('247.105'))))
    else:  # if from drop is other than Square kilometer, we first convert it to Square kilometer
        # then to required unit
        if from_unit == 'square meter':
            entry_value = str(Decimal(entry_value) / Decimal('1e+6'))
        elif from_unit == 'square mile':
            entry_value = str(Decimal(entry_value) / Decimal('0.386102'))
        elif from_unit == 'square yard':
            entry_value = str(Decimal(entry_value) / Decimal('1.196e+6'))
        elif from_unit == 'square foot':
            entry_value = str(Decimal(entry_value) / Decimal('1.076e+7'))
        elif from_unit == 'square inch':
            entry_value = str(Decimal(entry_value) / Decimal('1.55e+9'))
        elif from_unit == 'hectare':
            entry_value = str(Decimal(entry_value) / Decimal('100'))
        else:
            entry_value = str(Decimal(entry_value) / Decimal('247.105'))
        from_unit = 'square kilometer'
        area_entry_changing(entry_value)


def datarate_entry_changing(entry_value):
    global from_unit
    # if from drop is 'kilobit per second'
    if from_unit == 'kilobit per second':
        if to_unit == 'bit per second':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1000'))))
        elif to_unit == 'byte per second':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('125'))))
        elif to_unit == 'kilobit per second':
            to_value.set(cleaning(entry_value))
        elif to_unit == 'kilobyte per second':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('0.125'))))
        elif to_unit == 'kibibit per second':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('0.976563'))))
        elif to_unit == 'megabit per second':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('0.001'))))
        elif to_unit == 'megabyte per second':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('0.000125'))))
        elif to_unit == 'mebibit per second':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('0.000953674'))))
        elif to_unit == 'gigabit per second':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1e-6'))))
        elif to_unit == 'gigabyte per second':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1.25e-7'))))
        elif to_unit == 'gibibit per second':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('9.3132e-7'))))
        elif to_unit == 'terabit per second':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1e-9'))))
        elif to_unit == 'terabyte per second':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1.25e-10'))))
        elif to_unit == 'tebibit per second':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('9.0949e-10'))))
    else:  # if from drop is other than 'kilobit per second', we first convert it to it, then to required unit
        if from_unit == 'bit per second':
            entry_value = str(Decimal(entry_value) / Decimal('1000'))
        elif from_unit == 'byte per second':
            entry_value = str(Decimal(entry_value) / Decimal('125'))
        elif from_unit == 'kilobyte per second':
            entry_value = str(Decimal(entry_value) / Decimal('0.125'))
        elif from_unit == 'kibibit per second':
            entry_value = str(Decimal(entry_value) / Decimal('0.976563'))
        elif from_unit == 'megabit per second':
            entry_value = str(Decimal(entry_value) / Decimal('0.001'))
        elif from_unit == 'megabyte per second':
            entry_value = str(Decimal(entry_value) / Decimal('0.000125'))
        elif from_unit == 'mebibit per second':
            entry_value = str(Decimal(entry_value) / Decimal('0.000953674'))
        elif from_unit == 'gigabit per second':
            entry_value = str(Decimal(entry_value) / Decimal('1e-6'))
        elif from_unit == 'gigabyte per second':
            entry_value = str(Decimal(entry_value) / Decimal('1.25e-7'))
        elif from_unit == 'gibibit per second':
            entry_value = str(Decimal(entry_value) / Decimal('9.3132e-7'))
        elif from_unit == 'terabit per second':
            entry_value = str(Decimal(entry_value) / Decimal('1e-9'))
        elif from_unit == 'terabyte per second':
            entry_value = str(Decimal(entry_value) / Decimal('1.25e-10'))
        else:
            entry_value = str(Decimal(entry_value) / Decimal('9.0949e-10'))
        from_unit = 'kilobit per second'
        datarate_entry_changing(entry_value)


def digistore_entry_changing(entry_value):
    global from_unit
    # if from drop is 'kilobyte'
    if from_unit == 'kilobyte':
        if to_unit == 'bit':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('8000'))))
        elif to_unit == 'kilobit':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('8'))))
        elif to_unit == 'kibibit':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('7.8125'))))
        elif to_unit == 'megabit':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('0.008'))))
        elif to_unit == 'mebibit':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('0.00762939'))))
        elif to_unit == 'gigabit':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('8e-6'))))
        elif to_unit == 'gibibit':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('7.4506e-6'))))
        elif to_unit == 'terabit':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('8e-9'))))
        elif to_unit == 'tebibit':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('7.276e-9'))))
        elif to_unit == 'petabit':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('8e-12'))))
        elif to_unit == 'pebibit':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('7.1054e-12'))))
        elif to_unit == 'byte':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1000'))))
        elif to_unit == 'kilobyte':
            to_value.set(cleaning(entry_value))
        elif to_unit == 'kibibyte':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('0.976563'))))
        elif to_unit == 'megabyte':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('0.001'))))
        elif to_unit == 'mebibyte':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('0.000953674'))))
        elif to_unit == 'gigabyte':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1e-6'))))
        elif to_unit == 'gibibyte':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('9.3132e-7'))))
        elif to_unit == 'terabyte':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1e-9'))))
        elif to_unit == 'tebibyte':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('9.0949e-10'))))
        elif to_unit == 'petabyte':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1e-12'))))
        elif to_unit == 'pebibyte':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('8.8818e-13'))))
    else:  # if from drop is other than 'kilobyte', we first convert it to it, then to required unit
        if from_unit == 'bit':
            entry_value = str(Decimal(entry_value) / Decimal('8000'))
        elif from_unit == 'kilobit':
            entry_value = str(Decimal(entry_value) / Decimal('8'))
        elif from_unit == 'kibibit':
            entry_value = str(Decimal(entry_value) / Decimal('7.8125'))
        elif from_unit == 'megabit':
            entry_value = str(Decimal(entry_value) / Decimal('0.008'))
        elif from_unit == 'mebibit':
            entry_value = str(Decimal(entry_value) / Decimal('0.00762939'))
        elif from_unit == 'gigabit':
            entry_value = str(Decimal(entry_value) / Decimal('8e-6'))
        elif from_unit == 'gibibit':
            entry_value = str(Decimal(entry_value) / Decimal('7.4506e-6'))
        elif from_unit == 'terabit':
            entry_value = str(Decimal(entry_value) / Decimal('8e-9'))
        elif from_unit == 'tebibit':
            entry_value = str(Decimal(entry_value) / Decimal('7.276e-9'))
        elif from_unit == 'petabit':
            entry_value = str(Decimal(entry_value) / Decimal('8e-12'))
        elif from_unit == 'pebibit':
            entry_value = str(Decimal(entry_value) / Decimal('7.1054e-12'))
        elif from_unit == 'byte':
            entry_value = str(Decimal(entry_value) / Decimal('1000'))
        elif from_unit == 'kibibyte':
            entry_value = str(Decimal(entry_value) / Decimal('0.976563'))
        elif from_unit == 'megabyte':
            entry_value = str(Decimal(entry_value) / Decimal('0.001'))
        elif from_unit == 'mebibyte':
            entry_value = str(Decimal(entry_value) / Decimal('0.000953674'))
        elif from_unit == 'gigabyte':
            entry_value = str(Decimal(entry_value) / Decimal('1e-6'))
        elif from_unit == 'gibibyte':
            entry_value = str(Decimal(entry_value) / Decimal('9.3132e-7'))
        elif from_unit == 'terabyte':
            entry_value = str(Decimal(entry_value) / Decimal('1e-9'))
        elif from_unit == 'tebibyte':
            entry_value = str(Decimal(entry_value) / Decimal('9.0949e-10'))
        elif from_unit == 'petabyte':
            entry_value = str(Decimal(entry_value) / Decimal('1e-12'))
        else:
            entry_value = str(Decimal(entry_value) / Decimal('8.8818e-13'))
        from_unit = 'kilobyte'
        digistore_entry_changing(entry_value)


def energy_entry_changing(entry_value):
    global from_unit
    # if from drop is 'electronvolt'
    if from_unit == 'electronvolt':
        if to_unit == 'Joule':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1.6022e-19'))))
        elif to_unit == 'Kilojoule':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1.6022e-22'))))
        elif to_unit == 'Gram calorie':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('3.8293e-20'))))
        elif to_unit == 'Kilo calorie':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('3.8293e-23'))))
        elif to_unit == 'watt hour':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('4.4505e-23'))))
        elif to_unit == 'kilowatt hour':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('4.4505e-26'))))
        elif to_unit == 'electronvolt':
            to_value.set(cleaning(entry_value))
        elif to_unit == 'British thermal unit':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1.5186e-22'))))
        elif to_unit == 'US therm':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1.5189e-27'))))
        elif to_unit == 'Foot-pound':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1.1817e-19'))))
    else:  # if from drop is other than 'electronvolt', we first convert it to it, then to required unit
        if from_unit == 'Joule':
            entry_value = str(Decimal(entry_value) / Decimal('1.6022e-19'))
        elif from_unit == 'Kilojoule':
            entry_value = str(Decimal(entry_value) / Decimal('1.6022e-22'))
        elif from_unit == 'Gram calorie':
            entry_value = str(Decimal(entry_value) / Decimal('3.8293e-20'))
        elif from_unit == 'Kilo calorie':
            entry_value = str(Decimal(entry_value) / Decimal('3.8293e-23'))
        elif from_unit == 'watt hour':
            entry_value = str(Decimal(entry_value) / Decimal('4.4505e-23'))
        elif from_unit == 'kilowatt hour':
            entry_value = str(Decimal(entry_value) / Decimal('4.4505e-26'))
        elif from_unit == 'British thermal unit':
            entry_value = str(Decimal(entry_value) / Decimal('1.5186e-22'))
        elif from_unit == 'US therm':
            entry_value = str(Decimal(entry_value) / Decimal('1.5189e-27'))
        else:
            entry_value = str(Decimal(entry_value) / Decimal('1.1817e-19'))
        from_unit = 'electronvolt'
        energy_entry_changing(entry_value)


def freq_entry_changing(entry_value):
    global from_unit
    # if from_drop is 'Kilohertz'
    if from_unit == 'Kilohertz':
        if to_unit == 'Hertz':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1000'))))
        elif to_unit == 'Kilohertz':
            to_value.set(cleaning(entry_value))
        elif to_unit == 'Megahertz':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('0.001'))))
        elif to_unit == 'Gigahertz':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1e-6'))))
    else:  # if from drop is other than 'Kilohertz', we first convert it to it then to required unit
        if from_unit == 'Hertz':
            entry_value = str(Decimal(entry_value) / Decimal('1000'))
        elif from_unit == 'Megahertz':
            entry_value = str(Decimal(entry_value) / Decimal('0.001'))
        else:
            entry_value = str(Decimal(entry_value) / Decimal('1e-6'))
        from_unit = 'Kilohertz'
        freq_entry_changing(entry_value)


def fuel_entry_changing(entry_value):
    global from_unit
    # if from_drop is 'kilometer per liter'
    if from_unit == 'kilometer per liter':
        if to_unit == 'Miles per gallon':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('2.35215'))))
        elif to_unit == 'Miles per gallon (imperial)':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('2.82481'))))
        elif to_unit == 'kilometer per liter':
            to_value.set(cleaning(entry_value))
        elif to_unit == 'Liter per 100 kilometer':
            if Decimal(entry_value) != 0:
                to_value.set(cleaning(str(Decimal('100') / Decimal(entry_value))))
            else:
                to_value.set('')
    else:  # if from drop is other than 'kilometer per liter', we first convert it to it then to required unit
        if from_unit == 'Miles per gallon':
            from_unit = 'kilometer per liter'
            entry_value = str(Decimal(entry_value) / Decimal('2.35215'))
            fuel_entry_changing(entry_value)
        elif from_unit == 'Miles per gallon (imperial)':
            from_unit = 'kilometer per liter'
            entry_value = str(Decimal(entry_value) / Decimal('2.82481'))
            fuel_entry_changing(entry_value)
        else:
            if Decimal(entry_value) != 0:
                from_unit = 'kilometer per liter'
                entry_value = str(Decimal('100') / Decimal(entry_value))
                fuel_entry_changing(entry_value)
            else:
                to_value.set('')


def angle_entry_changing(entry_value):
    global from_unit
    # if from_drop is 'Degree'
    if from_unit == 'Degree':
        if to_unit == 'Degree':
            to_value.set(cleaning(entry_value))
        elif to_unit == 'Gradian':
            to_value.set(cleaning(str(Decimal(entry_value) * (Decimal('200') / Decimal('180')))))
        elif to_unit == 'Milliradian':
            to_value.set(cleaning(str(
                Decimal(entry_value) * ((Decimal('1000') * Decimal('3.141592653')) / Decimal('180')))))
        elif to_unit == 'Minute of arc':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('60'))))
        elif to_unit == 'Radian':
            to_value.set(cleaning(str(Decimal(entry_value) * (Decimal('3.141592653') / Decimal('180')))))
        elif to_unit == 'Second of arc':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('3600'))))
    else:  # if from drop is other than 'Degree', we first convert it to it then to required unit
        if from_unit == 'Gradian':
            entry_value = str(Decimal(entry_value) / (Decimal('200') / Decimal('180')))
        elif from_unit == 'Milliradian':
            entry_value = str(Decimal(entry_value) / ((Decimal('1000') * Decimal('3.141592653')) / Decimal('180')))
        elif from_unit == 'Minute of arc':
            entry_value = str(Decimal(entry_value) / Decimal('60'))
        elif from_unit == 'Radian':
            entry_value = str(Decimal(entry_value) / (Decimal('3.141592653') / Decimal('180')))
        else:
            entry_value = str(Decimal(entry_value) / Decimal('3600'))
        from_unit = 'Degree'
        angle_entry_changing(entry_value)


def pressure_entry_changing(entry_value):
    global from_unit
    # if from_drop is 'Pascal'
    if from_unit == 'Pascal':
        if to_unit == 'Bar':
            to_value.set(cleaning(str(Decimal(entry_value) * Decimal('1e-5'))))
        elif to_unit == 'Pascal':
            to_value.set(cleaning(entry_value))
        elif to_unit == 'pound per square inch':
            to_value.set(cleaning(str(Decimal(entry_value) / Decimal('6895'))))
        elif to_unit == 'Standard atmosphere':
            to_value.set(cleaning(str(Decimal(entry_value) / Decimal('101325'))))
        elif to_unit == 'Torr':
            to_value.set(cleaning(str(Decimal(entry_value) / Decimal('133'))))
    else:  # if from drop is other than 'Pascal', we first convert it to it then to required unit
        if from_unit == 'Bar':
            entry_value = str(Decimal(entry_value) / Decimal('1e-5'))
        elif from_unit == 'pound per square inch':
            entry_value = str(Decimal(entry_value) * Decimal('6895'))
        elif from_unit == 'Standard atmosphere':
            entry_value = str(Decimal(entry_value) * Decimal('101325'))
        else:
            entry_value = str(Decimal(entry_value) * Decimal('133'))
        from_unit = 'Pascal'
        pressure_entry_changing(entry_value)


def speed_entry_changing(entry_value):
    global from_unit
    # if from_drop is 'kilometer per hour'
    if from_unit == 'kilometer per hour':
        if to_unit == 'miles per hour':
            to_value.set(cleaning(str(Decimal(entry_value) / Decimal('1.609'))))
        elif to_unit == 'foot per second':
            to_value.set(cleaning(str(Decimal(entry_value) / Decimal('1.097'))))
        elif to_unit == 'meter per second':
            to_value.set(cleaning(str(Decimal(entry_value) / Decimal('3.6'))))
        elif to_unit == 'kilometer per hour':
            to_value.set(cleaning(entry_value))
        elif to_unit == 'Knot':
            to_value.set(cleaning(str(Decimal(entry_value) / Decimal('1.852'))))
    else:  # if from drop is other than 'kilometer per hour', we first convert it to it then to required unit
        if from_unit == 'miles per hour':
            entry_value = str(Decimal(entry_value) * Decimal('1.609'))
        elif from_unit == 'foot per second':
            entry_value = str(Decimal(entry_value) * Decimal('1.097'))
        elif from_unit == 'meter per second':
            entry_value = str(Decimal(entry_value) * Decimal('3.6'))
        else:
            entry_value = str(Decimal(entry_value) * Decimal('1.852'))
        from_unit = 'kilometer per hour'
        speed_entry_changing(entry_value)


# -------------------------------------------------------------

# functions for volume entry changing


def type_four_volume(value):
    if to_unit == 'cubic foot':
        to_value.set(cleaning(value))
    elif to_unit == 'cubic inch':
        to_value.set(cleaning(str(Decimal(value) * Decimal('1728'))))


def type_three_volume(value):
    if to_unit == 'imperial gallon':
        to_value.set(cleaning(value))
    elif to_unit == 'imperial quart':
        to_value.set(cleaning(str(Decimal(value) * Decimal('4'))))
    elif to_unit == 'imperial pint':
        to_value.set(cleaning(str(Decimal(value) * Decimal('8'))))
    elif to_unit == 'imperial cup':
        to_value.set(cleaning(str(Decimal(value) * Decimal('16'))))
    elif to_unit == 'imperial fluid ounce':
        to_value.set(cleaning(str(Decimal(value) * Decimal('160'))))
    elif to_unit == 'imperial tablespoon':
        to_value.set(cleaning(str(Decimal(value) * Decimal('256'))))
    elif to_unit == 'imperial teaspoon':
        to_value.set(cleaning(str(Decimal(value) * Decimal('768'))))


def type_two_volume(value):
    if to_unit == 'US liquid gallon':
        to_value.set(cleaning(value))
    elif to_unit == 'US liquid quart':
        to_value.set(cleaning(str(Decimal(value) * Decimal('4'))))
    elif to_unit == 'US liquid pint':
        to_value.set(cleaning(str(Decimal(value) * Decimal('8'))))
    elif to_unit == 'US legal cup':
        to_value.set(cleaning(str(Decimal(value) * Decimal('15.7725'))))
    elif to_unit == 'fluid ounce':
        to_value.set(cleaning(str(Decimal(value) * Decimal('128'))))
    elif to_unit == 'US tablespoon':
        to_value.set(cleaning(str(Decimal(value) * Decimal('256'))))
    elif to_unit == 'US teaspoon':
        to_value.set(cleaning(str(Decimal(value) * Decimal('768'))))


def type_one_volume(value):
    if to_unit == 'liter':
        to_value.set(cleaning(value))
    elif to_unit == 'milliliter':
        to_value.set(cleaning(str(Decimal(value) * Decimal('1000'))))
    elif to_unit == 'cubic meter':
        to_value.set(cleaning(str(Decimal(value) * Decimal('0.001'))))


a_type = ['liter', 'milliliter', 'cubic meter']
b_type = ['US liquid gallon', 'US liquid quart', 'US liquid pint', 'US legal cup',
          'fluid ounce', 'US tablespoon', 'US teaspoon']
c_type = ['imperial gallon', 'imperial quart', 'imperial pint', 'imperial cup',
          'imperial fluid ounce', 'imperial tablespoon', 'imperial teaspoon']
d_type = ['cubic foot', 'cubic inch']


def volume_entry_changing(entry_value):
    global from_unit, a_type, b_type, c_type, d_type

    if from_unit in a_type:
        if from_unit == 'milliliter':
            entry_value = str(Decimal(entry_value) / Decimal('1000'))
        elif from_unit == 'cubic meter':
            entry_value = str(Decimal(entry_value) / Decimal('0.001'))
        from_unit = 'liter'
        if to_unit in a_type:
            type_one_volume(entry_value)
        elif to_unit in b_type:
            entry_value = str(Decimal(entry_value) / Decimal('3.785'))
            type_two_volume(entry_value)
        elif to_unit in c_type:
            entry_value = str(Decimal(entry_value) / Decimal('4.546'))
            type_three_volume(entry_value)
        else:
            entry_value = str(Decimal(entry_value) / Decimal('28.317'))
            type_four_volume(entry_value)

    elif from_unit in b_type:
        if from_unit == 'US liquid quart':
            entry_value = str(Decimal(entry_value) / Decimal('4'))
        elif from_unit == 'US liquid pint':
            entry_value = str(Decimal(entry_value) / Decimal('8'))
        elif from_unit == 'US legal cup':
            entry_value = str(Decimal(entry_value) / Decimal('15.7725'))
        elif from_unit == 'fluid ounce':
            entry_value = str(Decimal(entry_value) / Decimal('128'))
        elif from_unit == 'US tablespoon':
            entry_value = str(Decimal(entry_value) / Decimal('256'))
        elif from_unit == 'US teaspoom':
            entry_value = str(Decimal(entry_value) / Decimal('768'))
        from_unit = 'US liquid gallon'
        if to_unit in a_type:
            entry_value = str(Decimal(entry_value) * Decimal('3.785'))
            type_one_volume(entry_value)
        elif to_unit in b_type:
            type_two_volume(entry_value)
        elif to_unit in c_type:
            entry_value = str(Decimal(entry_value) / Decimal('1.201'))
            type_three_volume(entry_value)
        else:
            entry_value = str(Decimal(entry_value) / Decimal('7.481'))
            type_four_volume(entry_value)

    elif from_unit in c_type:
        if from_unit == 'imperial quart':
            entry_value = str(Decimal(entry_value) / Decimal('4'))
        elif from_unit == 'imperial pint':
            entry_value = str(Decimal(entry_value) / Decimal('8'))
        elif from_unit == 'imperial cup':
            entry_value = str(Decimal(entry_value) / Decimal('16'))
        elif from_unit == 'imperial fluid ounce':
            entry_value = str(Decimal(entry_value) / Decimal('160'))
        elif from_unit == 'imperial tablespoon':
            entry_value = str(Decimal(entry_value) / Decimal('256'))
        elif from_unit == 'imperial teaspoom':
            entry_value = str(Decimal(entry_value) / Decimal('768'))
        from_unit = 'imperial gallon'
        if to_unit in a_type:
            entry_value = str(Decimal(entry_value) * Decimal('4.546'))
            type_one_volume(entry_value)
        elif to_unit in b_type:
            entry_value = str(Decimal(entry_value) * Decimal('1.201'))
            type_two_volume(entry_value)
        elif to_unit in c_type:
            type_three_volume(entry_value)
        else:
            entry_value = str(Decimal(entry_value) / Decimal('6.229'))
            type_four_volume(entry_value)

    elif from_unit in d_type:
        if from_unit == 'cubic inch':
            entry_value = str(Decimal(entry_value) / Decimal('1728'))
        from_unit = 'cubic foot'
        if to_unit in a_type:
            entry_value = str(Decimal(entry_value) * Decimal('28.371'))
            type_one_volume(entry_value)
        elif to_unit in b_type:
            entry_value = str(Decimal(entry_value) * Decimal('7.481'))
            type_two_volume(entry_value)
        elif to_unit in c_type:
            entry_value = str(Decimal(entry_value) * Decimal('6.229'))
            type_three_volume(entry_value)
        else:
            type_four_volume(entry_value)


# ----------------------------------------------------------------------------------------


# validate functions checks whether the entered string is a valid number (no alphabets, special characters...)
def validate(strings):
    flag = 1
    for letter in strings:
        if letter in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', 'e',
                      'E', '+', '-'] and strings.count('.') <= 1 and (int(strings.count('e'))
                                                                      + int(strings.count('E'))) <= 1:
            pass
        else:
            flag = 0
            break

    if strings[-1] in ['e', 'E', '+', '-'] or strings[0] in ['e', 'E']:
        flag = 0

    if flag == 0:
        return False
    else:
        return True


# from entry modifying
def from_entry_change(from_result):
    global from_unit, to_unit
    from_unit = from_drop.get()
    to_unit = to_drop.get()
    entry_value = from_result.get()
    if len(entry_value) != 0 and entry_value != '.' and validate(entry_value):
        if unit_type_drop.get() == 'Length':
            length_entry_changing(entry_value)
        elif unit_type_drop.get() == 'Mass':
            mass_entry_changing(entry_value)
        elif unit_type_drop.get() == 'Time':
            time_entry_changing(entry_value)
        elif unit_type_drop.get() == 'Temperature':
            temp_entry_changing(entry_value)
        elif unit_type_drop.get() == 'Area':
            area_entry_changing(entry_value)
        elif unit_type_drop.get() == 'Data Transfer Rate':
            datarate_entry_changing(entry_value)
        elif unit_type_drop.get() == 'Digital Storage':
            digistore_entry_changing(entry_value)
        elif unit_type_drop.get() == 'Energy':
            energy_entry_changing(entry_value)
        elif unit_type_drop.get() == 'Frequency':
            freq_entry_changing(entry_value)
        elif unit_type_drop.get() == 'Fuel Economy':
            fuel_entry_changing(entry_value)
        elif unit_type_drop.get() == 'Plane Angle':
            angle_entry_changing(entry_value)
        elif unit_type_drop.get() == 'Pressure':
            pressure_entry_changing(entry_value)
        elif unit_type_drop.get() == 'Speed':
            speed_entry_changing(entry_value)
        else:
            volume_entry_changing(entry_value)


# equation label setting
def label_setting():
    global from_unit, to_unit
    from_unit = from_drop.get()

    if len(from_entry.get()) != 0 and validate(from_entry.get()):
        if unit_type_selection != 'Temperature' and (from_unit and to_unit) != 'Liter per 100 kilometer':
            if from_entry.get() == '.' or Decimal(from_entry.get()) == 0:
                equation.config(text='1 ' + from_unit + ' = ' + to_unit)
            else:
                a = Decimal(to_entry.get()) / Decimal(from_entry.get())
                equation.config(text='1 ' + from_unit + ' = ' + cleaning(str(a)) + ' ' + to_unit)
        elif unit_type_selection == 'Fuel Economy':
            if from_entry.get() == '.' or Decimal(from_entry.get()) == 0:
                a = ''
                equation.config(text='1 ' + from_unit + ' = ' + to_unit)
            elif (from_unit or to_unit) == 'Miles per gallon':
                a = Decimal('235.215') / Decimal(from_entry.get())
            elif (from_unit or to_unit) == 'Miles per gallon (imperial)':
                a = Decimal('282.481') / Decimal(from_entry.get())
            else:
                a = Decimal('100') / Decimal(from_entry.get())
            equation.config(text='1 ' + from_unit + ' = ' + cleaning(str(a)) + ' ' + to_unit)
        else:
            if from_unit == to_unit:
                equation.config(text='1 ' + from_unit + ' = 1 ' + to_unit)
            elif from_unit == 'Celsius':
                if to_unit == 'Fahrenheit':
                    equation.config(text='1 Celsius = (1 * 9/5) + 32 = 33.8 Fahrenheit')
                else:
                    equation.config(text='1 Celsius = 1 + 273.15 = 274.15 Kelvin')
            elif from_unit == 'Fahrenheit':
                if to_unit == 'Celsius':
                    equation.config(text='1 Fahrenheit = (1 - 32) * 5/9 = -17.22 Celsius')
                else:
                    equation.config(text='1 Fahrenheit = ((1 - 32) * 5/9) + 273.15 = 255.928 Kelvin')
            else:
                if to_unit == 'Kelvin':
                    equation.config(text='1 Kelvin = 1 - 273.15 = -272.15 Celsius')
                else:
                    equation.config(text='1 Kelvin = (1 - 273.15) * 9/5 + 32 = -457.87 Fahrenheit')


# from/to dropdown modifying
def unit_modified(index, value, op):
    from_entry_change(from_entry)
    label_setting()


# action for copy button
def copy_to_value():
    copied_text = to_entry.get()
    window.clipboard_clear()
    window.clipboard_append(copied_text)


# ----------------------------------------------------------------------------------------
# all options in all dropdowns
options = ["Length", "Mass", "Time", "Temperature", "Area",
           "Data Transfer Rate", "Digital Storage", "Energy",
           "Frequency", "Fuel Economy", "Plane Angle",
           "Pressure", "Speed", "Volume"]
length_options = ["Kilometer", "Meter", "Centimeter", "Millimeter", "Micrometer", "Nanometer", "Picometer",
                  "Mile", "Yard", "Foot", "Inch", "Nautical mile"]
mass_options = ["tonne", "Kilogram", "Gram", "Milligram", "Microgram", "Imperial ton",
                "US ton", "Stone", "Pound", "Ounce"]
time_options = ["Nanosecond", "Microsecond", "Millisecond", "Second", "Minute", "Hour", "Day",
                "Week", "Month", "Calendar year", "Decade", "Century"]
temp_options = ["Celsius", "Fahrenheit", "Kelvin"]
area_options = ["square kilometer", "square meter", "square mile", "square yard",
                "square foot", "square inch", "hectare", "acre"]
data_rate_options = ["bit per second", "byte per second", "kilobit per second",
                     "kilobyte per second", "kibibit per second", "megabit per second",
                     "megabyte per second", "mebibit per second", "gigabit per second",
                     "gigabyte per second", "gibibit per second", "terabit per second",
                     "terabyte per second", "tebibit per second"]
dig_store_options = ["bit", "kilobit", "kibibit", "megabit", "mebibit", "gigabit", "gibibit",
                     "terabit", "tebibit", "petabit", "pebibit", "byte", "kilobyte", "kibibyte",
                     "megabyte", "mebibyte", "gigabyte", "gibibyte", "terabyte", "tebibyte",
                     "petabyte", "pebibyte"]
energy_options = ['Joule', 'Kilojoule', 'Gram calorie', 'Kilo calorie', 'watt hour',
                  'kilowatt hour', 'electronvolt', 'British thermal unit', 'US therm',
                  'Foot-pound']
freq_options = ['Hertz', 'Kilohertz', 'Megahertz', 'Gigahertz']
fuel_economy_options = ["Miles per gallon", 'Miles per gallon (imperial)',
                        'kilometer per liter', 'Liter per 100 kilometer']
plane_angle_options = ['Degree', 'Gradian', 'Milliradian', 'Minute of arc',
                       'Radian', 'Second of arc']
pressure_options = ['Bar', 'Pascal', 'pound per square inch', 'Standard atmosphere', 'Torr']
speed_options = ['miles per hour', 'foot per second', 'meter per second', 'kilometer per hour',
                 'Knot']
volume_options = ['US liquid gallon', 'US liquid quart', 'US liquid pint',
                  'US legal cup', 'fluid ounce', 'US tablespoon', 'US teaspoon',
                  'cubic meter', 'liter', 'milliliter', 'imperial gallon', 'imperial quart',
                  'imperial pint', 'imperial cup', 'imperial fluid ounce', 'imperial tablespoon',
                  'imperial teaspoon', 'cubic foot', 'cubic inch']

# unit type dropdown
unit_type_drop = ttk.Combobox(window, values=options)
unit_type_drop.current(0)
unit_type_drop.config(background="white", state="readonly", font="TimesNewRoman 10", width=30)
unit_type_drop.bind("<<ComboboxSelected>>", unit_select_action)

# from dropdown
from_sv = StringVar()
from_drop = ttk.Combobox(window, textvariable=from_sv, values=length_options)
from_drop.current(0)
from_drop.config(background="white", state="readonly", font="TimesNewRoman 10", width=30)
from_sv.trace('w', unit_modified)

# to dropdown
to_sv = StringVar()
to_drop = ttk.Combobox(window, textvariable=to_sv, values=length_options)
to_drop.current(1)
to_drop.config(background="white", state="readonly", font="TimesNewRoman 10", width=30)
to_sv.trace('w', unit_modified)

# swap button and label widget
swap_button = Button(window, text='--->', anchor=CENTER, command=swap_units)
swap_label = Label(window, text='SWAP', font="Arial 9", anchor=CENTER, fg="black")

# from entry widget
from_value = StringVar()
from_value.set('1')
from_value.trace("w", lambda name, index, mode, from_result=from_value: from_entry_change(from_result))
from_entry = Entry(window, font="TimesNewRoman 11", justify=CENTER, width=28, textvariable=from_value)

# to entry widget
to_value = StringVar()
to_value.set('1000')
to_entry = Entry(window, font="TimesNewRoman 11", justify=CENTER, width=28, state="readonly", textvariable=to_value)

# equation display widget
equation = Label(window, text='1 kilometer = 1000 meter', font='Arial 11')
copy_button = Button(window, text='copy', command=copy_to_value)

# packing all on window
unit_type_drop.grid(row=0, column=0, pady=10)
from_drop.grid(row=1, column=0, pady=10, padx=15)
from_entry.grid(row=2, column=0, pady=5)
swap_button.grid(row=1, column=1, padx=10)
swap_label.grid(row=2, column=1)
to_drop.grid(row=1, column=2, padx=15)
to_entry.grid(row=2, column=2)
equation.grid(row=3, columnspan=3, pady=18)
copy_button.grid(row=2, column=3)

window.mainloop()
