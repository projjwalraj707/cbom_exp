import python
import semmle.crypto.Crypto
import semmle.python.dataflow.new.DataFlow
import semmle.python.ApiGraphs

from DataFlow::CallCfgNode call, DataFlow::ExprNode expr
where
	call = API::moduleImport("Crypto").getMember("PublicKey").getMember("RSA").getMember("generate").getACall() and
	DataFlow::localFlow(expr, call.getArg(0)) and
	expr.asExpr().(Num).getN() = ["256"]
select call, expr, expr.asExpr().(Num).getN()