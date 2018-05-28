import numpy

def kernelz(x, y, z, model):
    '''
    Calculate the first z-derivative of a 1/r function.

    Inputs:
    x, y, z - numpy arrays - observation points (meters)
    model - list - values of x, y, z and r of a sphere

    Output:
    diffz - numpy array - first z derivative
    '''
    
    # Condition
    assert x.size == y.size, ('All arrays must have the same size')
    assert y.size == z.size, ('All arrays must have the same size')
    assert x.size == z.size, ('All arrays must have the same size')
    
    # Sphere values 
    xe, ye, ze, radius = model

    # Computing the kernel at z direction
    v = (4./3.)*(numpy.pi)*(radius)**3
    r = numpy.sqrt((x - xe)**2 + (y - ye)**2 + (z - ze)**2)
    diffz = -((z - ze)/(r**3)) * v
    # Return the final output
    return diffz

def kernelxx(x, y, z, model):
    '''
    Calculate the second x-derivative of a 1/r function.

    Inputs:
    x, y, z - numpy arrays - observation points (meters)
    model - list - values of x, y, z and r of a sphere

    Output:
    diffxx - numpy array - first z derivative
    '''
    
    # Condition
    assert x.size == y.size, ('All arrays must have the same size')
    assert y.size == z.size, ('All arrays must have the same size')
    assert x.size == z.size, ('All arrays must have the same size')
    
    # Sphere values 
    xe, ye, ze, radius = model

    # Computing the kernel
    v = (4./3.)*(numpy.pi)*(radius)**3
    r = numpy.sqrt((x - xe)**2 + (y - ye)**2 + (z - ze)**2)
    diffxx = (((3.*(x - xe)**2)/(r**5)) - (1./(r**3))) * v
    
    # Return the final outpu
    return diffxx

def kernelxy(x, y, z, model):
    '''
    Calculate the second xy-derivative of a 1/r function.

    Inputs:
    x, y, z - numpy arrays - observation points (meters)
    model - list - values of x, y, z and r of a sphere

    Output:
    diffxy - numpy array - first z derivative
    '''
    
    # Condition
    assert x.size == y.size, ('All arrays must have the same size')
    assert y.size == z.size, ('All arrays must have the same size')
    assert x.size == z.size, ('All arrays must have the same size')
    
    # Sphere values 
    xe, ye, ze, radius = model

    # Computing the kernel
    v = (4./3.)*(numpy.pi)*(radius)**3
    r = numpy.sqrt((x - xe)**2 + (y - ye)**2 + (z - ze)**2)
    diffxy = 3. * (((x - xe) * (y - ye))/(r**5)) * v
    return diffxy


def kernelxz(x, y, z, model):
    '''
    Calculate the second xz-derivative of a 1/r function.

    Inputs:
    x, y, z - numpy arrays - observation points (meters)
    model - list - values of x, y, z and r of a sphere

    Output:
    diffxz - numpy array - first z derivative
    '''
    
    # Condition
    assert x.size == y.size, ('All arrays must have the same size')
    assert y.size == z.size, ('All arrays must have the same size')
    assert x.size == z.size, ('All arrays must have the same size')
    
    # Sphere values 
    xe, ye, ze, radius = model

    # Computing the kernel
    v = (4./3.)*(numpy.pi)*(radius)**3
    r = numpy.sqrt((x - xe)**2 + (y - ye)**2 + (z - ze)**2)
    diffxz = 3. * (((x - xe) * (z - ze)) / (r**5))
    
    # Return the final output
    return diffxz

def kernelyy(x, y, z, model):
    '''
    Calculate the second y-derivative of a 1/r function.

    Inputs:
    x, y, z - numpy arrays - observation points (meters)
    model - list - values of x, y, z and r of a sphere

    Output:
    diffz - numpy array - first z derivative
    '''
    
    # Condition
    assert x.size == y.size, ('All arrays must have the same size')
    assert y.size == z.size, ('All arrays must have the same size')
    assert x.size == z.size, ('All arrays must have the same size')
    
    # Sphere values 
    xe, ye, ze, radius = model

    # Computing the kernel
    v = (4./3.)*(numpy.pi)*(radius)**3
    r = numpy.sqrt((x - xe)**2 + (y - ye)**2 + (z - ze)**2)
    diffyy = ((3.*(y - ye)**2) / (r**5)) - (1./(r**3)) * v
    
    # Return the final output
    return diffyy

def kernelyz(x, y, z, model):
    '''
    Calculate the second yz-derivative of a 1/r function.

    Inputs:
    x, y, z - numpy arrays - observation points (meters)
    model - list - values of x, y, z and r of a sphere

    Output:
    diffyz - numpy array - first z derivative
    '''
    
    # Condition
    assert x.size == y.size, ('All arrays must have the same size')
    assert y.size == z.size, ('All arrays must have the same size')
    assert x.size == z.size, ('All arrays must have the same size')
    
    # Sphere values 
    xe, ye, ze, radius = model

    # Computing the kernel
    v = (4./3.)*(numpy.pi)*(radius)**3
    r = numpy.sqrt((x - xe)**2 + (y - ye)**2 + (z - ze)**2)
    diffyz = 3. * (((y - ye) * (z - ze)) / (r**5)) * v
    
    # Return the final output
    return diffyz

def kernelzz(x, y, z, model):
    '''
    Calculate the second xy-derivative of a 1/r function.

    Inputs:
    x, y, z - numpy arrays - observation points (meters)
    model - list - values of x, y, z and r of a sphere

    Output:
    diffzz - numpy array - first z derivative
    '''
    
    # Condition
    assert x.size == y.size, ('All arrays must have the same size')
    assert y.size == z.size, ('All arrays must have the same size')
    assert x.size == z.size, ('All arrays must have the same size')
    
    # Sphere values 
    xe, ye, ze, radius = model

    # Computing the kernel
    v = (4./3.)*(numpy.pi)*(radius)**3
    r = numpy.sqrt((x - xe)**2 + (y - ye)**2 + (z - ze)**2)
    diffzz = (((3. * (z - ze)**2) / (r**5)) - (1./(r**3))) * v

    # Return the final output
    return diffzz
