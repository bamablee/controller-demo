//
// Copyright (c) 2018 Bryson Lee. All rights reserved.
//
// A Meyers singleton that mocks a set of 1024 32-bit
// device registers located at 0xD0000000.
//

class Registers
{
private:
  // ctor is private 'cuz we're a singleton...
  Registers() : base_(0xD0000000), regs_{0} {};
  
  uint32_t base_;
  uint32_t regs_[1024];

public:
  static Registers& instance()
  {
    static Registers instance;
    return instance;
  };

  // mutator / accessor
  void set( uint32_t reg, uint32_t val );
  uint32_t get( uint32_t reg ) const;

  // forbid copying...
  Registers( Registers const & ) = delete;
  Registers & operator=( Registers const & ) = delete;

};
