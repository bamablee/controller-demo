//
// Copyright (c) 2018 Bryson Lee. All rights reserved.
//

// This define suppresses auto_ptr deprecation warnings from Boost
// when compiling under C++11
#define BOOST_NO_AUTO_PTR

#include <boost/python.hpp>

#include "fan.hh"
#include "registers.hh"

namespace bp = boost::python;

BOOST_PYTHON_MODULE(_tempcontrol_ext)
{
  // expose the NVI-pattern Fan abstract base class
  bp::class_<Fan, boost::noncopyable >("fan", bp::no_init)
    .def("set_speed", &Fan::set_speed)
    .add_property("speed", &Fan::get_speed)
    .add_property("name", &Fan::get_name)
    ;

  // expose the PWM_Fan implementation class
  // all the methods available from Python come from the NVI base
  bp::class_<PWM_Fan, bp::bases<Fan>, boost::noncopyable >("pwm_fan", bp::init<std::string, uint32_t, uint32_t, double>())
    ;

  // expose register accessor/mutator
  bp::def( "get_reg", +[](uint32_t r){ return Registers::instance().get(r);} );
  bp::def( "set_reg", +[](uint32_t r, uint32_t v) { Registers::instance().set( r, v );} );

}
