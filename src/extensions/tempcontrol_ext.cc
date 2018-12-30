//
//
//

#define BOOST_NO_AUTO_PTR

#include <boost/python.hpp>

#include "fan.hh"

namespace bp = boost::python;

BOOST_PYTHON_MODULE(_tempcontrol_ext)
{
  bp::class_<Fan, boost::noncopyable >("Fan", bp::no_init)
    .def("set_speed", &Fan::set_speed)
    .add_property("speed", &Fan::get_speed)
    .add_property("name", &Fan::get_name)
    ;

  bp::class_<PWM_Fan, bp::bases<Fan>, boost::noncopyable >("PWM_Fan", bp::init<std::string, uint32_t, uint32_t, double>())
    ;

}
