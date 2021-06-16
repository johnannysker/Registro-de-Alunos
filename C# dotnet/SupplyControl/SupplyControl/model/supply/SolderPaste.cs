using SupplyControl.interfaces;

namespace SupplyControl.model.supply
{
    public class SolderPaste : SupplyBase, ISupply
    {
        public SolderPaste(string code) : base(code)
        {

        }

        public string GetCode()
        {
            return base.code;
        }
    }
}
