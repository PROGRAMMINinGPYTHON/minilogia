(window.QJP=window.QJP||[]).push([["n11s_lazy"],{FdmV:function(t,i,e){"use strict";e.d(i,"a",(function(){return o}));var n=e("peh1");function o(t,i){return Object(n.createSelector)((i=>i.get(t)),((t,i)=>i),(t=>t),Object(n.createStructuredSelector)(i))}},WKau:function(t,i,e){"use strict";e.r(i),e.d(i,"default",(function(){return D}));var n=e("Vg22"),o=e("YDJX"),a=e("WHvC"),r=e("JPcv"),s=e.n(r),c=e("q1tI"),l=e.n(c),p=e("WSi9"),d=e("l9T1"),u=(e("4mDm"),e("3bBZ"),e("pVnL")),h=e.n(u),m=e("1Pxe"),f=e("TSYQ"),N=e.n(f),v=e("JxFz"),A=e("bvRJ"),C=e("a08m");class E extends l.a.PureComponent{constructor(t){super(t),this.handlePrimaryClickAction=t=>{this.props.onClickPrimaryAction&&this.props.onClickPrimaryAction(t),this.handleHide()},this.handleSecondaryClickAction=t=>{this.props.onClickSecondaryAction&&this.props.onClickSecondaryAction(t),this.handleHide()},this.handleClose=()=>{this.props.onClose&&this.props.onClose(),this.handleHide()},this.handleHide=()=>{this.props.onHide&&this.props.onHide({id:this.props.id})},this.props.duration>0&&(this.autoHideTimeout=window.setTimeout(this.handleHide,this.props.duration))}componentWillUnmount(){clearTimeout(this.autoHideTimeout)}renderActions(){return l.a.createElement("div",{className:"UINotification-actions"},this.props.primaryActionLabel?l.a.createElement("div",{className:"UINotification-primaryAction"},"upsell"===this.props.variant?l.a.createElement(C.a,{onClick:this.handlePrimaryClickAction},this.props.primaryActionLabel):l.a.createElement(v.a,{onClick:this.handlePrimaryClickAction},this.props.primaryActionLabel)):null,this.props.secondaryActionLabel?l.a.createElement("div",{className:"UINotification-secondaryAction"},l.a.createElement(C.a,{onClick:this.handleSecondaryClickAction},this.props.secondaryActionLabel)):null)}render(){var t=N()("UINotification","UINotification--"+this.props.variant);return l.a.createElement("div",{className:t},this.props.icon?l.a.createElement("div",{className:"UINotification-iconWrap"},l.a.createElement(A.a,{className:"UINotification-icon",icon:this.props.icon})):null,"upsell"===this.props.variant?l.a.createElement("span",{"aria-label":"gift-emoji",className:"UINotification-emoji",role:"img"},"🎁"):null,l.a.createElement("div",{className:"UINotification-content"},null!==this.props.title?l.a.createElement("div",{className:"UINotification-title"},this.props.title):null,l.a.createElement("div",{className:"UINotification-message"},this.props.message),this.renderActions()),this.props.isDismissible?l.a.createElement("div",{className:"UINotification-hideIconWrap",onClick:this.handleClose},l.a.createElement(A.a,{className:"UINotification-hideIcon",icon:"x-inverse"})):null)}}E.defaultProps={isDismissible:!1,variant:"default"};var I=e("zK28"),y=(e("E9XD"),e("pn57")),g=e("FdmV");class O extends c.PureComponent{constructor(){super(...arguments),this.handleHide=t=>{var{id:i}=t;this.props.actions.removeNotification({id:i})},this.handleClose=()=>{if(this.props.notification){var t=this.props.notification.get("onClose");t&&t()}}}componentDidMount(){I.a.NotificationContainer={addNotification:this.props.actions.addNotification,removeNotification:this.props.actions.removeNotification},QLoad("Quizlet.NotificationContainer")}renderNotification(){return l.a.createElement(E,h()({},this.props.notification.toJS(),{key:this.props.notification.get("id"),onClose:this.handleClose,onHide:this.handleHide}))}render(){return l.a.createElement("div",{className:"NotificationContainer"},l.a.createElement(m.CSSTransitionGroup,{transitionEnterTimeout:600,transitionLeaveTimeout:300,transitionName:"NotificationContainer-notification-"},this.props.notification?[this.renderNotification()]:[]))}}var b=Object(g.a)("notifications",{notification:t=>t.get("notifications").reduce(((t,i)=>i.get("priority")>t.get("priority")?i:t))}),T=Object(n.connect)(b,(t=>({actions:Object(y.bindActionCreators)({addNotification:d.a,removeNotification:d.c},t)})))(O),U=e("xhj2");function D(){var t=Object(o.handleActions)(d.b,s.a.Map({notifications:s.a.List()}));U.a.register({notifications:t});var i=window.document.createElement("div");window.document.body.appendChild(i),Object(a.a)(l.a.createElement(n.Provider,{store:U.b},l.a.createElement(l.a.Fragment,null,l.a.createElement(T,null),l.a.createElement(p.a,null))),i)}},WSi9:function(t,i,e){"use strict";(function(t){e("yXV3");var n=e("og3H"),o=e("Ef4P"),a=e("PHlw"),r=e("zK28"),s=e("Ilu8"),c=e("goAZ"),l=e("q1tI"),p=e("Vg22"),d=e("peh1"),u=["Upgrade/success"];class h extends l.Component{componentDidMount(){var i;-1===u.indexOf(r.a.actionString)&&r.a.didJustUpgrade&&this.props.user&&this.props.user.type!==n.dc.NO_UPGRADE&&(this.props.user.type===n.dc.GO?i=t("upgrade_success.notification.upgrade_type_go"):this.props.user.type===n.dc.PLUS?i=t("upgrade_success.notification.upgrade_type_plus"):this.props.user.type===n.dc.TEACHER&&(i=t("upgrade_success.notification.upgrade_type_teacher")),Object(s.a)({duration:c.a.DEFAULT,icon:"check",isDismissible:!1,message:t("upgrade_success.notification.message",{upgradeType:i})}))}render(){return null}}var m=Object(d.createStructuredSelector)({user:a.f});i.a=Object(p.connect)(m,null,null,{context:o.a})(h)}).call(this,e("nrsj").default)},l9T1:function(t,i,e){"use strict";e.d(i,"b",(function(){return l})),e.d(i,"a",(function(){return p})),e.d(i,"c",(function(){return d}));e("JfAA");var n=e("YDJX"),o=e("JPcv"),a=e.n(o),r=e("goAZ"),s=e("mEm4"),c=Object(s.a)("NOTIFICATIONS",{ADD_NOTIFICATION:null,REMOVE_NOTIFICATION:null}),l={[c.ADD_NOTIFICATION]:(t,i)=>{var{payload:e}=i;return t.update("notifications",(t=>t.push(e)))},[c.REMOVE_NOTIFICATION]:(t,i)=>{var{payload:e}=i;return t.update("notifications",(t=>t.filter((t=>(!e.id||e.id!==t.get("id"))&&(!e.type||e.type!==t.get("type"))))))}},p=Object(n.createAction)(c.ADD_NOTIFICATION,(t=>a.a.Map({priority:r.b.DEFAULT,duration:r.a.DEFAULT}).merge(t).set("id",Math.random().toString()))),d=Object(n.createAction)(c.REMOVE_NOTIFICATION)}}]);