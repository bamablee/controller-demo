//
// Copyright (c) 2018 Bryson Lee. All rights reserved.
//

#include <string>

// Use the non-volatile interface pattern to define what
// an actuator looks like to users and developers

class Actuator
{
public:
  virtual ~Actuator() = default;

  // public interface methods for users
  void write( double pct_output );
  double read();
  std::string name() const;

  // forbid copying...
  Actuator( Actuator const & ) = delete;
  Actuator & operator=( Actuator const & ) = delete;

protected:
  // allow construction only in derived classes
  Actuator( const std::string &name );

private:
  // private methods for derived classes
  virtual void do_write( double ) = 0;
  virtual double do_read() = 0;

  std::string name_;
  
};
