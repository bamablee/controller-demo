//
// Copyright (c) 2018 Bryson Lee. All rights reserved.
//

#include <string>
#include <cstdint>

#include "actuator.hh"

class PWM_Fan : public Actuator
{
public:
  PWM_Fan( const std::string& name,
	   uint32_t pwm_max,
	   uint32_t pwm_addr,
	   double   rpm_max );

  virtual ~PWM_Fan();

private:
  void do_write( double pctspeed ) final;
  double do_read() final;

  uint32_t pwm_max_;
  uint32_t pwm_addr_;
  double   rpm_max_;

  uint32_t pwm_;

};
